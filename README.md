# TimeSeries
# Language: Python
# Input: TXT
# Output: CSV
# Tested with: PluMA 1.1, Python 3.6

PluMA plugin to apply static properties to time series data

The plugin accepts as input a TXT file of keyword-value pairs, tab-delimited:
static: CSV file of static properties of samples
dynamic: Time series data in CSV format

The static CSV file is assumed to contain one row per sample, with each sample identified by a unique ID:
sample_id, staticproperty1, staticproperty2, etc.

In the dynamic CSV file, rows are assumed to contain time-series data, meaning each sample can appear multiple times.  The assumption is that sample identifiers will have the following structure:

sample_id-1, dynamicproperty1, dynamicproperty2, etc.
sample_id-2, dynamicproperty1, dynamicproperty2, etc.

It then will append the static properties of each sample_id to the end of *every* time series sample involving sample_id.

