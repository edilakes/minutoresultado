# Extrae metadatos de las bases Access mediante DAO, en SOLO LECTURA y modo compartido.
# Salida: datos\metadatos_be.json y datos\metadatos_fe.json
# Uso:  powershell -ExecutionPolicy Bypass -File herramientas\extraer_metadatos.ps1
param(
    [string]$Be = $(if ($env:MR_DB_BE) { $env:MR_DB_BE } else { '\\nas.cifs.cti-sevilla.sas.junta-andalucia.es\SSCC-CONSTITUCION-1\SSCC\Sb-ServiciosGestionCentros\FondosEuropeos\Database_be.accdb' }),
    [string]$Fe = $(if ($env:MR_DB_FE) { $env:MR_DB_FE } else { 'C:\Users\lagosedgar20p\Desktop\Database_fe.accdb' }),
    [string]$Salida = (Join-Path (Split-Path -Parent $PSScriptRoot) 'datos')
)
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force -Path $Salida | Out-Null

function Get-Prop($obj, $name) {
    try { return [string]$obj.Properties[$name].Value } catch { return $null }
}

function Get-Tablas($db, [bool]$OmitirVinculadas = $false) {
    foreach ($t in $db.TableDefs) {
        if ($t.Name -like 'MSys*' -or $t.Name -like '~*') { continue }
        if ($OmitirVinculadas -and [string]$t.Connect) {
            # Tabla vinculada: sus campos se leen en el backend (evita ir al NAS una por una).
            [ordered]@{
                nombre = $t.Name; vinculada = $true
                origen = [string]$t.SourceTableName; conexion = [string]$t.Connect
                descripcion = $null; campos = @(); indices = @()
            }
            continue
        }
        $campos = @(foreach ($f in $t.Fields) {
            [ordered]@{
                nombre      = $f.Name
                tipo        = [int]$f.Type
                tamano      = [int]$f.Size
                requerido   = [bool]$f.Required
                descripcion = (Get-Prop $f 'Description')
                defecto     = [string]$f.DefaultValue
                regla       = [string]$f.ValidationRule
            }
        })
        $indices = @(foreach ($i in $t.Indexes) {
            [ordered]@{
                nombre   = $i.Name
                primario = [bool]$i.Primary
                unico    = [bool]$i.Unique
                campos   = @(foreach ($c in $i.Fields) { $c.Name })
            }
        })
        # El recuento de filas se hace por ODBC (herramientas\inventario.py); aquí es lento.
        [ordered]@{
            nombre      = $t.Name
            vinculada   = [bool]$t.Connect
            origen      = [string]$t.SourceTableName
            conexion    = [string]$t.Connect
            descripcion = (Get-Prop $t 'Description')
            campos      = $campos
            indices     = $indices
        }
    }
}

function Get-Relaciones($db) {
    foreach ($r in $db.Relations) {
        [ordered]@{
            nombre        = $r.Name
            tabla         = $r.Table
            tabla_foranea = $r.ForeignTable
            atributos     = [int]$r.Attributes
            campos        = @(foreach ($f in $r.Fields) { [ordered]@{ campo = $f.Name; campo_foraneo = $f.ForeignName } })
        }
    }
}

function Get-Consultas($db) {
    foreach ($q in $db.QueryDefs) {
        if ($q.Name -like '~*') { continue }
        [ordered]@{
            nombre = $q.Name
            tipo   = [int]$q.Type
            sql    = $q.SQL
        }
    }
}

function Get-Documentos($db, $contenedor) {
    try { @(foreach ($d in $db.Containers[$contenedor].Documents) { $d.Name }) } catch { @() }
}

$motor = New-Object -ComObject DAO.DBEngine.120

# ---- Backend ----
$db = $motor.OpenDatabase($Be, $false, $true)
try {
    $metaBe = [ordered]@{
        ruta       = $Be
        extraccion = (Get-Date -Format 's')
        tablas     = @(Get-Tablas $db)
        relaciones = @(Get-Relaciones $db)
        consultas  = @(Get-Consultas $db)
    }
} finally { $db.Close() }
$metaBe | ConvertTo-Json -Depth 8 | Out-File -Encoding utf8 (Join-Path $Salida 'metadatos_be.json')
"BE: $($metaBe.tablas.Count) tablas, $($metaBe.relaciones.Count) relaciones, $($metaBe.consultas.Count) consultas"

# ---- Frontend ----
$db = $motor.OpenDatabase($Fe, $false, $true)
try {
    $metaFe = [ordered]@{
        ruta        = $Fe
        extraccion  = (Get-Date -Format 's')
        tablas      = @(Get-Tablas $db $true)
        relaciones  = @(Get-Relaciones $db)
        consultas   = @(Get-Consultas $db)
        formularios = @(Get-Documentos $db 'Forms')
        informes    = @(Get-Documentos $db 'Reports')
        modulos     = @(Get-Documentos $db 'Modules')
        macros      = @(Get-Documentos $db 'Scripts')
    }
} finally { $db.Close() }
$metaFe | ConvertTo-Json -Depth 8 | Out-File -Encoding utf8 (Join-Path $Salida 'metadatos_fe.json')
"FE: $($metaFe.tablas.Count) tablas, $($metaFe.consultas.Count) consultas, $($metaFe.formularios.Count) formularios, $($metaFe.informes.Count) informes, $($metaFe.modulos.Count) modulos, $($metaFe.macros.Count) macros"
