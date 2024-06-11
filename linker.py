#!/usr/bin/env python3

import pandas as pd

blast_output = pd.read_csv('664UCJSG016-Alignment-HitTable.csv', header=None)

blast_output.columns = [
    'query_id', 'subject_id', 'percent_identity', 'alignment_length',
    'mismatches', 'gap_openings', 'query_start', 'query_end',
    'subject_start', 'subject_end', 'e_value', 'bit_score',
    'query_coverage', 'subject_coverage', 'frame'
]

circos_links = pd.DataFrame({
    'chr1': 'chr1',
    'start1': blast_output['query_start'],
    'end1': blast_output['query_end'],
    'chr2': 'chr2',
    'start2': blast_output['subject_start'],
    'end2': blast_output['subject_end']
})

circos_links.to_csv('circos_links.txt', sep='\t', index=False, header=False)
