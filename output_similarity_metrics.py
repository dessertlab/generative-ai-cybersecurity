import evaluate
import pylcs
import os
import numpy as np
from rouge import Rouge
import bleu_score

meteor = evaluate.load('meteor')
bleu = evaluate.load('bleu')

def edit_dist(hyp, ref):
    tmp = pylcs.edit_distance(hyp, ref)
    res_norm = 1 - (tmp / max(len(hyp), len(ref)))
    return res_norm

def calc_ed(hyps, refs):
    scores = [edit_dist(h, r) for h, r in zip(hyps, refs)]
    mean_ed = np.mean(scores)
    formatted_score = f'ED: {mean_ed * 100:.2f}%'
    print(formatted_score)
    return formatted_score

def calc_meteor(hyps, refs):
    scores = [meteor.compute(predictions=[h], references=[r])['meteor'] for h, r in zip(hyps, refs)]
    mean_meteor = np.mean(scores)
    formatted_score = f'METEOR: {mean_meteor * 100:.2f}%'
    print(formatted_score)
    return formatted_score

def calc_rouge(hyps, refs):
    metrics = ["rouge-1", "rouge-2", "rouge-3", "rouge-4", "rouge-l"]
    formatted_score = []
    for metric in metrics:
        rouge = Rouge(metrics=[metric])
        scores = rouge.get_scores(hyps, refs, avg=True)
        mean_rouge = scores[metric]['f']
        formatted_score.append(f'{metric.upper()}: {mean_rouge * 100:.2f}%')
    for score in formatted_score:
        print(score)
    return formatted_score

def calc_EM(hyps, refs):
    scores = [1 if hyp.split() == ref.split() else 0 for hyp, ref in zip(hyps, refs)]
    mean_em = np.mean(scores)
    formatted_score = f'EM: {mean_em * 100:.2f}%'
    print(formatted_score)
    return formatted_score

def calc_corpus_BLEU(hyps, refs):
    formatted_score = []
    for i in range(1, 5):
        bleu_tup = bleu_score.compute_bleu([[x] for x in refs], hyps, smooth=False, max_order=i)
        bleu = bleu_tup[0]
        formatted_score.append(f'BLEU-{i}: {bleu * 100:.2f}%')
    for score in formatted_score:
        print(score)
    return formatted_score

def read_files(hyps_name, refs_name):
    refs = []
    hyps = []
    
    with open(refs_name, 'r') as refs_file:
        refs_temp = refs_file.readlines()
        refs += [ref.strip('\n') for ref in refs_temp]
    
    with open(hyps_name, 'r') as hyps_file:
        hyps_temp = hyps_file.readlines()
        hyps += [hyp.strip('\n') for hyp in hyps_temp]
    
    return hyps, refs

if __name__ == '__main__':
    refs = []
    hyps = []

    files_hyps = ["results/output_persona.out"]  # FILE NAME, change to the name of the model output file
    #files_hyps = ["results/output_few_shot.out"]  # FILE NAME, change to the name of the model output file
    files_refs = ["results/subset.out"]  # FILE NAME, change to the name of the file containing the correct snippets

    for fh, fr in zip(files_hyps, files_refs):
        print('\n', fh, fr, '\n')
        hyps, refs = read_files(fh, fr)

        ed_score = calc_ed(hyps, refs)
        corpus_bleu_score = calc_corpus_BLEU(hyps, refs)
        rouge_score = calc_rouge(hyps, refs)
        meteor_score = calc_meteor(hyps, refs)
        em_score = calc_EM(hyps, refs)

        # Save the scores to a text file
        output_filename = "subset_output_persona.txt"  # Change this
        #output_filename = "subset_output_few_shot.txt"  # Change this
        output_filepath = os.path.join("results", output_filename)

        with open(output_filepath, 'w') as f:
            f.write(ed_score + "\n")
            f.write("\n".join(corpus_bleu_score) + "\n")
            f.write("\n".join(rouge_score) + "\n")
            f.write(meteor_score + "\n")
            f.write(em_score + "\n")
