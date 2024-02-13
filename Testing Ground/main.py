from bio_seq import bio_seq

text_dna = bio_seq("ATCG", "DNA")
print(text_dna.get_seq_info())
text_dna.random(100, "RNA")
print(text_dna.get_seq_info())
print(text_dna.count_kmer())
print(text_dna.transcription())
print(text_dna.rev_transcription())
print(text_dna.reverse_complementary())
print(text_dna.duplex())

print(text_dna.gc_content())
print(text_dna.gc_splice_content(10))
print(text_dna.translation())
print(text_dna.codon_usage("A"))
print(text_dna.reading_frame_gen())
for rf in text_dna.orf_proteins_gen(30,70):
    print(rf)