> generate.py => dataset generation
usage :

```bash
 python3 generate.py https://github.com/juspay/hyperswitch \
                                                   -f sft -m 100 -o hyperswitch_final -b main
```
(-m flag represent no of lines you want around the patch)


train:
```bash
 python3 train_sft.py \
                                              --dataset archit11/hyperswitch-rust-commits-final2 \
                                               --model Qwen/Qwen3-4B \
                                               --output_dir ./qwen-rust-full-ft \
                                               --batch_size 2 \
                                               --gradient_accumulation 2 \
                                               --learning_rate 5e-6 \
                                               --num_epochs 2 \
                                               --wandb_project rust-hyperswitch-fullft \
                                               --wandb_run_name qwen3-4b-fullft-run1
```
