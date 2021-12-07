for f in reformatted-unicode/*
do
    lang=$(basename $f)
    echo $lang
    phonetisaurus-train --lexicon "$f/$lang-train-high" --seq2_del
    phonetisaurus-apply --model train/model.fst --word_list "$f/$lang-test" > output/lang
done