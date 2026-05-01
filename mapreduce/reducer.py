#!/usr/bin/env python3
"""
REDUCER: Receives sorted (key, value) pairs and sums up counts per key.
This is the 'final tallier' — group by class, sum all the 1's.
"""
import sys

current_pclass = None
current_count = 0

# Hadoop guarantees mapper output arrives SORTED by key
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        pclass, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue
    
    if current_pclass == pclass:
        # Same class as before — keep adding
        current_count += count
    else:
        # Class changed — output the previous total
        if current_pclass is not None:
            print(f"Class {current_pclass}\t{current_count}")
        current_pclass = pclass
        current_count = count

# Last group ?
if current_pclass is not None:
    print(f"Class {current_pclass}\t{current_count}")