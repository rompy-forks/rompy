import os

# Define datasource types to be used. Note that including SourceDataset will break the
# specification as this object cannot be serialised, but this does not cause any problems
# working in a python environement
DATA_SOURCE_TYPES = os.getenv(
    "DATA_SOURCE_TYPES",
    "SourceDataset:rompy.core.data,SourceFile:rompy.core.data,SourceIntake:rompy.core.data,SourceDatamesh:rompy.core.data",
)

BOUNDARY_SOURCE_TYPES = os.getenv("BOUNDARY_SOURCE_TYPES", DATA_SOURCE_TYPES)
SPEC_BOUNDARY_SOURCE_TYPES = os.getenv(
    "SPEC_BOUNDARY_SOURCE_TYPES",
    DATA_SOURCE_TYPES + ",SourceWavespectra:rompy.core.boundary",
)
