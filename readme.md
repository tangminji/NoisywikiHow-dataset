# NoisywikiHow Dataset
a Benchmark for Learning with Real-world Noisy Labels in Natural Language Processing

## Data
### Structure
+ data
    + wikihow           NoisywikiHow Dataset
        + noisy/        The input folder
            + train.csv                         The clean training data. Format `choosen_id, step_id, cat_id, step, cat`
            + val.csv                           The clean validation data. Format `choosen_id, step_id, cat_id, step, cat`
            + test.csv                          The clean testing data. Format `choosen_id, step_id, cat_id, step, cat`
            + mix_{0.1,0.2,0.4,0.6}.csv         **NoisywikiHow** training data with real-world label noise for main trial "Analysis the LNL methods on real-world label noise" in Section 4.2 and Section 4.4.
                +   Format `choosen_id, step_id, noisy_id, cat_id, step, cat, noisy_step, noisy_cat, noisy_label`.
                +   Take `(noisy_id, cat_id)` as input.
            + sym_{0.1,0.2,0.4,0.6}.csv         Comparative training data with symmetric label noise for trial "Analysis the LNL methods on real-world label noise" in Section 4.5. 
                +   Format `choosen_id,step_id,cat_id,noisy_label,step,cat,noisy_cat`.
                +   Take `(step_id, noisy_label)` as input.
            + {tail,uncommon,neighbor}_0.1.csv  Training data with different noise sources of real-world noise for trial "Analysis the LNL methods under different noise source" in Section 4.3.
                +   Format is the same as `mix_0.1.csv`.
        + cat158.csv    The choosen 158 event intention classes.

### Fields description

| Field         | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `choosen_id`  | **global id** for this sample. range from 0~89142            |
| `step`        | The real step text.                                          |
| `step_id`     | The id for `step`                                            |
| `cat`         | The real event intention category text.                      |
| `cat_id`      | The id for `cat`                                             |
| `noisy_step`  | The **corrupted** step text with **certain noise rate**. It may be agree with `step`,  may not either. |
| `noisy_cat`   | For noise on labels(`sym`, etc.):  The **corrupted** event intention label with **certain noise rate**. It may be agree with `cat`,  may not either.<br />For similar noisy steps(`mix`,`tail`,`uncommon`,`neighbor`):  The event intention category correspond to `noisy step`. |
| `noisy_label` | The id for `noisy_cat`. `-1` for the category out of given 158 classes (OOV class). |

Put this folder under `NoisywikiHow/data` and rename as `wikihow` before running!