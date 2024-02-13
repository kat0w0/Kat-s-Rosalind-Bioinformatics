motif = "peanuts"
Seq = "peanpeappaeapeapeapeappanutustnsutnsutnspeanutsuuusususususs"
Seq2 = "pppppepppapnsuttusneappeanuts"
Seq_list = [Seq, Seq2]

print(all(motif in s for s in Seq_list))
