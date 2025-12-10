set -e

## Generate tables
python3 data_gen/gen_char_tasks.py --task=spell
python3 data_gen/gen_char_tasks.py --task=spell_rand
python3 data_gen/gen_char_tasks.py --task=spell_inverse
python3 data_gen/gen_char_tasks.py --task=spell_inverse_rand
python3 data_gen/gen_char_tasks.py --task=contains_char
python3 data_gen/gen_char_tasks.py --task=contains_char_rand
python3 data_gen/gen_char_tasks.py --task=ins_char
python3 data_gen/gen_char_tasks.py --task=ins_char_rand
python3 data_gen/gen_char_tasks.py --task=del_char
python3 data_gen/gen_char_tasks.py --task=del_char_rand
python3 data_gen/gen_char_tasks.py --task=swap_char
python3 data_gen/gen_char_tasks.py --task=swap_char_rand
python3 data_gen/gen_char_tasks.py --task=sub_char
python3 data_gen/gen_char_tasks.py --task=sub_char_rand

#python3 data_gen/gen_sem_orth.py

python3 data_gen/gen_word_tasks.py --task=contains_word
python3 data_gen/gen_word_tasks.py --task=ins_word
python3 data_gen/gen_word_tasks.py --task=del_word
python3 data_gen/gen_word_tasks.py --task=swap_word
python3 data_gen/gen_word_tasks.py --task=sub_word


## Format & write in Dolma format
python3 gen_dolma_format.py