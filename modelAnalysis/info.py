#######################################################################################
# DEFINITIONS

# Metabolite (verbose to model) definitions
metDict = {
    'atp': 'ATP[c]',        # ATP,              ChEBI 15422
    'ctp': 'CTP[c]',        # CTP,              ChEBI 17677
    'gtp': 'GTP[c]',        # GTP,              ChEBI 15996
    'utp': 'UTP[c]',        # UTP,              ChEBI 15713
    'A': 'L_Alanine[c]',        # Alanine,          ChEBI 16977
    'R': 'L_Arginine[c]',        # Arginine,         ChEBI 16467
    'N': 'L_Asparagine[c]',        # Asparagine,       ChEBI 17196
    'D': 'L_Aspartate[c]',        # Aspartate,        ChEBI 17053
    'C': 'L_Cysteine[c]',        # Cysteine,         ChEBI 17561
    'Q': 'L_Glutamine[c]',        # Glutamine,        ChEBI 18050
    'E': 'L_Glutamate[c]',        # Glutamate,        ChEBI 16015
    'G': 'Glycine[c]',          # Glycine,          ChEBI 15428
    'H': 'L_Histidine[c]',        # Histidine,        ChEBI 15971
    'I': 'L_Isoleucine[c]',        # Isoleucine,       ChEBI 17191
    'L': 'L_Leucine[c]',        # Leucine,          ChEBI 15603
    'K': 'L_Lysine[c]',        # Lysine,           ChEBI 18019
    'M': 'L_Methionine[c]',        # Methionine,       ChEBI 16643
    'F': 'L_Phenylalanine[c]',        # Phenylalanine,    ChEBI 17295
    'P': 'L_Proline[c]',        # Proline,          ChEBI 17203
    'S': 'L_Serine[c]',        # Serine,           ChEBI 17115
    'T': 'L_Threonine[c]',        # Threonine,        ChEBI 16857
    'W': 'L_Tryptophan[c]',        # Tryptophan,       ChEBI 16828
    'Y': 'L_Tyrosine[c]',        # Tyrosine,         ChEBI 17895
    'V': 'L_Valine[c]',        # Valine,           ChEBI 16414
    'h2o': 'H2O[c]',        # H2O
    'adp': 'ADP[c]',        # ADP
    'Pi': 'Orthophosphate[c]',          # Phosphate
    'h': 'H[c]',            # Hydrogen [Proton]
    'PPi': 'Diphosphate[c]',        # Pyrophosphate
}

# Nucleotides Dictionary
ntpsDict = {
    'atp': 507.181,     # ATP,              ChEBI 15422
    'gtp': 483.15644,   # GTP,              ChEBI 17677
    'ctp': 523.18062,   # CTP,              ChEBI 15996
    'ttp': 484.14116,   # UTP,              ChEBI 15713 (TTP is psuedo for UTP in viral genome)
}
# Amino Acids Dictionary
aaDict = {
    'A': 89.09322,      # Alaline,          ChEBI 16977
    'R': 174.201,       # Arginine,         ChEBI 16467
    'N': 132.118,       # Asparagine,       ChEBI 17196
    'D': 133.1027,      # Aspartate,        ChEBI 17053
    'C': 121.158,       # Cysteine,         ChEBI 17561
    'Q': 146.14458,     # Glutamine,        ChEBI 18050
    'E': 147.1293,      # Glutamate,        ChEBI 16015
    'G': 75.06664,      # Glycine,          ChEBI 15428
    'H': 155.15468,     # Histidine,        ChEBI 15971
    'I': 131.17296,     # Isoleucine,       ChEBI 17191
    'L': 131.17296,     # Leucine,          ChEBI 15603
    'K': 146.18764,     # Lysine,           ChEBI 18019
    'M': 149.21238,     # Methionine,       ChEBI 16643
    'F': 165.18918,     # Phenylalanine,    ChEBI 17295
    'P': 115.1305,      # Proline,          ChEBI 17203
    'S': 105.09262,     # Serine,           ChEBI 17115
    'T': 119.1192,      # Threonine,        ChEBI 16857
    'W': 204.22526,     # Tryptophan,       ChEBI 16828
    'Y': 181.18858,     # Tyrosine,         ChEBI 17895
    'V': 117.14638,     # Valine,           ChEBI 16414
}
# Misc. Dictionary
miscDict = {
    'PPi': 173.94332,   # Pyrophosphate,    ChEBI 18361
}
# Avogadro's Number
N_A         = 6.0221409e+23
# ATP requirement coefficients
# source: Queka, Dietmaira, Hanschob, Mart�neza, Borthb, Nielsen
# Journal of Biotechnology 184 (2014) 172�178
k_atp_protein = 4.3
k_atp_dna = 1.4
k_atp_rna = 0.4

k_ppi = 1
