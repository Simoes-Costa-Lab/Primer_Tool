python ./get_middle_genomic.py

#!/bin/bash
primer3_core --p3_settings_file=./primer3web_v4_0_0_genomic_settings_constrained.txt --output=Selected_Enhancers_toClone_primers.txt ./Selected_Enhancers_toClone_genomic.txt

python ./reduce_primers.py