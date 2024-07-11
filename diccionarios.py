## Nombres de parallel ##
P = {
    "EXT": "Extracción",
    "TRF": "Transformación",
    "LOD": "Cargue",
    "CHC": "Cambios B",
    "FRMW": "Framework",
    "PRPAL": "Principal",
    "UPD": "Actualizacion",
    "TRUN": "Truncado",
    "CDC": "Cambios",
    "DUP": "Duplicados",
    "LIM": "Limpieza",
    "CAR": "Cargue",
    "CTL": "Control",
    "DEL": "Eliminación",
    "EXEC": "Ejecución",
    "00": "Inicio CP4D",
    "01": "Extraccion CP4D",
    "02": "Transformaciones CP4D",
    "03": "Cargue CP4D",
    "04": "secuencias CP4D",
    "05": "CP4D",
    "06": "CP4D"
}
## Tipo Artefacto
T = {
    "JOB": "Parallel",
    "SEQ": "Secuencia",
    "001": "Folder CP4D",
    "002": "Folder 2 CP4D",
    "003": "Folder 3 CP4D",
    "004": "Folder 4 CP4D",
    "005": "Folder  5CP4D"
}
## Nombre secuencias
S = {
    "JOB": "Parallel",
    "SEQ": "Secuencia"
}
## Nombre de links
L = {
    "Lnk": "Nombre links"
}
## Nombre de stages
G = {
    "AGG": "PxAggregator",
    "CHC": "Change Capture B",
    "CAC": "Change Apply",
    "COP": "PxCopy",
    "FIL": "PxFilter",
    "FTP": "FTP",
    "FUN": "PxFunnel",
    "LKP": "LookUp",
    "MER": "Merge",
    "MOD": "Modify",
    "PIV": "Pivot",
    "RMD": "Remove Duplicates",
    "SCD": "Slowly Changing Dimension",
    "SRT": "Sort",
    "SKG": "Surrogate Key Generator",
    "SWT": "Switch",
    "CONT": "Container",
    "ORA": "OracleConnectorPX",
    "DB2": "DB2 Connector",
    "ODBC": "ODBC Connector",
    "SQL": "SQL Server Enterprise",
    "SYB": "Sybase",
    "SP": "Store Procedure",
    "TER": "Teradata",
    "COG": "Column Generator",
    "ROG": "Row Generator",
    "DS": "PxDataSet",
    "SF": "PxSequentialFile",
    "LFS": "Lookup File Set",
    "HF": "Hash File",
    "IPC": "Inter Process",
    "LNP": "Link Partitioner",
    "LNC": "Link Collector",
    "DTR": "Data Rule",
    "INV": "Investigate",
    "STD": "Standardize",
    "TRF": "CTransformerStage",
    "JN": "PxJoin",
    "ISD_Input": "Information Services Input",
    "ISD_Output": "Information Services Output",
    "HD": "Hierarchical Data",
    "PEEK": "Peek",
    "STL": "Start Loop Activity",
    "ENL": "End Loop Activity",
    "EXH": "CExceptionHandler",
    "CMD": "CExecCommandActivity",
    "NEC": "Nested Condition",
    "NOA": "Notification Activity",
    "RTN": "Routine Activity",
    "SEQ": "CSequencer",
    "TEA": "CTerminatorActivity",
    "UVA": "CUserVarsActivity",
    "WFF": "Wait For File Activity",
    "JOB": "CJobActivity",
    "CDC": "Change Capture P",
    "SCONT": "Container Popular",
    "MSS": "Sql Server,",
    "POG": "Conector",
    "JDBC": "Conector",
    "CLMN": "Conector"
}
## Rutas
R = {
    "RUTA_CARGA": "Rutas archivos carga",
    "RUTA_DSET": "Ruta DataSets",
    "RUTA_ENTRADA": "archivos insumos",
    "RUTA_RECHAZO": "archivos rechazos",
    "RUTA_SALIDA": "Archivos salida",
    "RUTA_SEQ": "Archivos secuencias",
    "RUTA_SH": "Archivos shell",
    "RUTA_TEMPORAL": "Archivos temporales",
    "RUTA_TRABAJO": "Archivo trabajo",
    "RUTA_LOG": "Archivos log",
    "RUTA_PROCESADO": "Archivos procesados",
    "RUTA_DATASET": "Ruta DataSets P",
    "PATH_ROOT_ENTRADA": "Ruta Root Entrada",
    "POG_DWH_SCHEMA_ADMSTAGE": "Ruta admsate",
    "POG_DWH_CONNECTIONSTRING": "Ruta conecciones",
    "PATH_ROOT_SALIDA": "Ruta salida cp",
    "POG_DWH_PASSWORD": "Ruta pasword",
    "POG_DWH_CONNECTIONSTRING_ODBC": "Ruta odbc",
    "POG_DWH_SCHEMA_DWHCFC": "Ruta shema",
    "PATH_ROOT_TRABAJO_SHELL": "Ruta shell",
    "POG_DWH_USER": "Ruta user dwh",
    "PATH_ROOT_DATASETS": "Ruta Root DataSets",
    "RUTA_PARAMETER_SET": "Ruta parameter set",
    "RUTA_ARCHIVO": "Ruta archivo set",
    "PATH_ROOT_TRABAJO": "Ruta Trabajo"

}
proyecto_bogota = {
    'Identifier "PAR_PATH_ROUTE"': "Rutas"
}
proyecto_popular = {
    'Identifier "PAR_ETL"': "Rutas"
}

def get_p():
    return P
def get_t():
    return T
def get_s():
    return S
def get_l():
    return L
def get_g():
    return G
def get_r():
    return R
def get_bogota():
    return proyecto_bogota
def get_popular():
    return proyecto_popular