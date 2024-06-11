#!/usr/bin/env python3

import pandas as pd

blast_output = pd.read_csv('664UCJSG016-Alignment-HitTable.csv', header=None)

blast_output.columns = [
    'query_id', 'subject_id', 'percent_identity', 'alignment_length',
    'mismatches', 'gap_openings', 'query_start', 'query_end',
    'subject_start', 'subject_end', 'e_value', 'bit_score',
    'query_coverage', 'subject_coverage', 'frame'
]

karyotype = pd.DataFrame({
    'chr': ['chr'] * len(blast_output['subject_id'].unique()),
    '-': ['-'] * len(blast_output['subject_id'].unique()),
    'id': blast_output['subject_id'].unique(),
    'label': blast_output['subject_id'].unique(),
    'start': [0] * len(blast_output['subject_id'].unique()),
    'end': [blast_output['subject_end'].max()] * len(blast_output['subject_id'].unique()),
    'color': blast_output['subject_id'].unique()
})

karyotype.to_csv('karyotype.txt', sep=' ', index=False, header=False)

hist = pd.DataFrame({
    'chr': blast_output['subject_id'],
    'start': blast_output['subject_start'],
    'end': blast_output['subject_end'],
    'value': [1] * len(blast_output)  
})

hist.to_csv('hist.txt', sep=' ', index=False, header=False)
