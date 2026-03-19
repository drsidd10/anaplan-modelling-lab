# Architecture

## Overview
This document describes the end-to-end architecture of the Anaplan Modeling Lab.

## Module Hierarchy
- Data Hub (data/)
- SYS Modules (src/lists, src/time)
- Input Modules (data/inputs)
- Calc Modules (src/modules)
- Output (notebooks)

## Data Flow
flowchart TD
  DataHub --> SYS --> INPUT --> CALC --> OUTPUT --> Exec_Dashboard
