# NoisyWikihow Dataset
A benchmark of controlled noise for Event Intention Classification.

## Data
+ data
    + wikihow           Noisywikihow Dataset
        + noisy/        The input folder
            + train.csv                         The clean train data. Format `choosen_id, step_id, cat_id, step, cat`
            + test.csv                          The clean test data. Format `choosen_id, step_id, cat_id, step, cat`
            + mix_{0.1,0.2,0.4,0.6}.csv         Noisywikihow train data with noise. Format `choosen_id, step_id, noisy_id, cat_id, step, cat, noisy_step, noisy_cat, noisy_label`.
                +   Take `(noisy_id, cat_id)` as input.
            + sym_{0.1,0.2,0.4,0.6}.csv         Train data with symmetric noise. Format `choosen_id,step_id,cat_id,noisy_label,step,cat,noisy_cat`.
                +   Take `(step_id, noisy_label)` as input.
            + {tail,uncommon,neighbor}_0.1.csv  Train data with different noise sources. Format is the same as `mix_0.1.csv`.
        + embedding     Preprocessed step embeddings for each models.
        + cat158.csv    The choosen 158 event intention classes.

Put this folder under Noisywikihow/data before running!