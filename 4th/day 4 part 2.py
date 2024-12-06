
def find_xmas(wordsearch):
    wordsearch = wordsearch.split("\n")
    total = 0
    for rowindex, row in enumerate(wordsearch[1:-1]):
        for index, letter in enumerate(row[1:-1]):
            if letter == "A":
                if ({wordsearch[rowindex][index], wordsearch[rowindex+2][index+2]} == {"M", "S"}
                    and {wordsearch[rowindex+2][index], wordsearch[rowindex][index+2]} == {"M", "S"}):
                    total += 1
    return total

input = """MSMMXMMAMXMAMSAMXMXXMMASAXAXAMXSXMASMXASXAXXMASMSXSAMXSMXMMXMMSMMSSSMSSSSSMMASXMAXXMASAMXMSXAXSAMXSXAMXSAMMMXMSMXSXMAMASMSAMXMSXMXSXMASXMAMX
ASAMXXAMAMXXMAMSMSMAXSAAMXMSMMAMXXMAXAXMXMMAXSMAXMMXMASAASXMXAAAXAAMAAAXAAXMASMMSAMXASAMSAMXXAXAXASMMAAAAXMMAMAAAXASAMMAMXSAMXSASASASASMSMMM
MXAMXXXMAAAMXSSXAASMMMMXSAAAAMSMXMXAMXMMSASMMMMMMXXAAAMSMMAXMMSSMMSMMMSMSSMMXMMAMXMMAXAMMAMMSMSMMXSASMMMXMASASMMMSMSASAAXAXXMAMAMMSAMXXAAXXX
XSXMMAXSXSXSAMXMSMSMAXMASMSMSMMAAAMXSAAXMAMXAAAAMMMMSMMAXXSMSXAAXAMXSAMMAAAXMSMXMAXXAXSMSSMAAAAAMASXMASMXMXSMXXAAMMSAMMSMMXMAMMAMXMMMSMSMSSS
MAMAXXXMAMMMMSAMXAXMSMMMSMXXMASMMSXASMSMMSASXXSASAXXAAXMSSMAMMXMMMMAMASMMSMMAAAMSMSMSMXAMXMSSSSSMASAMAMMXMASXSSMMSAMXMAXASXSAMMSMAXMAMXAAAAM
XASMMAMMAMXAASASMMMMAAAXXMXAMAMAXXMMSXMAAXMASAXASASMSSMXMASAXAMMAXMAMMMXMAASMMMMAXMAXAXMXMAAAAAXMXSMMSXMAMXSAAXXAMASXMASAMAMMSAAXMSMASXMMMSM
SAMAMMXSASMMMSXMAXSSSXMSMXMAMSMMMSAMXAMMMSMSMMMMMMMMAMAMSASXMMAMSXXASAAXMMMMAASMSXXAMMMSAMMXMMMMMMMAMAAMSSMMXMXMASMMMMAXAMXMAMXXMXXXXXXASAXX
AXSAMMAXXXAXAMMSSMMAMXAAAAMSMXAXAASMMXMAMAMAASMMASAMAMSAMXSASXSMAMSASMSSMXSMMMMAAAMSSMASXMAAMMMSAAMAMMSMMAMXAXSAMXXAAMMSMSXMAMASXMMMSMXMMAMA
MXSASMSSSSMMSSMXMMSASMSMSMMXAMXMXSMXSMSXSASMSMXSASASMSXMSXMAMMXMAXMAMXAXXAXXAXMMMMMMAMMSAMSMSAASXXSAMAAXMAMSXSSXMAMSSSMSAAMXSMAMSAAAAXXMAMMS
XMMAMAAXAAXAMAMAMMMAMXAAMXSMAMSSMAXAXAXASMSXAAAMMSMMXSMXMMMAMSAMMSSMMMMSMMMXXSMXAXMSAMSMMMXAMMXSAMSAMSMSSXMAMXMAMMMMAXAMMMXAMAMMSSMSSSMSASAX
MAMXMMMSSMMXSAMXXAAAMSMMMMMMMMAASMMMSMMMMAMMMMMSAXASXXAAMASAMMASAAAAXAASASASMMMSXSAXMSXAXMMAXSAMXAMMMMAMAMXXAASAMXSMMMXMXXMMSAMXXAXAMAAAAMAS
MXSXAXXXASXMMAMMSMXMAXMMSSMASMSMMXXXAAAXMAMXAXMMMMXMAMSXSXSASMMMMSSMSMXSAMASAAMAMMXMSMMMMXSAMAXMMAXAAMXMASXMXXSASASAMXMMMXMASAMXSMMXSSSMSMXM
AAMXMMSAMSMMSAMXAAASXMSAAAXAMXMXSXXSMSMSSMSSMSMAMSMAAMXXMAMMMAXXMAMXAMMMMMMSMMMASAMXAAAXAXMXXMAXMASMSSXSMMMSXASAMXSAMXMAAAMASMMASXMAMAMXXMAS
MXSASASAXXAASAMSMMMXAXMMSSMMSMMAAMASAAXAAAMXXAMAMAASXSXAXSMSSSSMMASXMMSAXAAMAMSAMXSSSSMMSXSMMSMMMAXXAMXMAAAMMMMXMAMXMASXSMSASAMASAMSSMSSMSAS
AAXAMXMXMMMMXMAMXAMXAMXAAXXAAAMASMAMSMMSMMMSMAMXXMMMXMMSMMAAAAAASAMMSASXSMXXAMMXMXMMMAXXXAAXAAASASMMMSASMMMSAXAAXXXMXMSAAXMMSXMXSXMAAXXAAMXS
XMMSMMSSMXAXXSAMSMSAMXMMMXMSSSXAMMXMAXMAMSAMASMMASAMAASXAMMMMMSMMASAMMSASAMSMXMAMAMMSAMXMMMMMSSMAMXMASASMAMMAMMSMMXSAXMMMAXMXMXAXMMMMMSMMMAS
MSAMAAAAMMSSXMAMAAMMMXMASXMXXAMXXAXSMSAMXMAXXXASASASXSMMMMMXXMMXSSMMSXMXMAMAAASXSMSAMASMSAAXXMXMAMASAMAMMAMAAMXAAAAMAMMAXMMSXMSSMMAXAXXMAMXS
XMAXMMSSMAAXASMMSXMASXSASAMSMMMMMSMSXMASXXMMXXAMASAMXAMXSASMMXMAMAMXXXXMSSXMSMSAAAMXSSMASMSMXMXMASXMAMSMSASXXSXSSSMSMMSASXAMAMAXASXSXMAMXXAM
XXSMSAXAMMSMXMAMAXMXSAMXSXMAASXSAXAXXXXMXAMSAMSMMMAMSXMAMMMASAMASAMMMXMXAXAXXAMXMMMAMAMXMAXMAXXSMXAMXMXXMASXMXAMAMAAXMXASMSMAMMMMMXAMXSMSMSS
MAMAMMSXMAMMXSAMMXSAMXMAMASXSMAAMMAMMSMXMSMAASMASXMMMAMXXSSMMASASXXAXSSMASXMMXMXSAXXMAMMMMMSSSMMSSSMSMSSMAMMAMXMAMSMMSMMMAMSMMXXXXXMAMAAAAAS
MAMAMXMMXXMAMSXSXMAXMAMASXMXAMSMXAXMMAASAAMSSMMAMAXAMXMAMXAXSAMXSAMMMAXMXMASAMXASXSMSMMAAXXAAXMAAXAMXAAXMXMASXMASMAXAXAAMAMMMMSAMXMMSAMXMSMS
MASMMMSMXSMMXSAMXMXASXSAXMMSXXAXXMMSXXSSSSXMAXMSSMXXXMMSASMMMMSXMMASMMMXASXSAMMXSASAAASXMSMMSMMMSXMAMMMSSXMAMASMMSXSSSSMSASXAAXAXXXAXAXMXMAX
XAMAAXAMASAXSMSMAMSXSAMMXAMXMSMSMSAMMMXMAXAMMMMMAXXSSMAAXAXAXXSXSMASAXMSMSMMAMXAMAMMMMMAAAXAAXMAMAXXSXXAMAMASAMAMXXMAXMASASMMSSMSMMMSMMMAMXM
MSSSMMAMAMAMXAAMAMAXMAASMSAAMAAAAMMSASMMSMSAXMXMASXAAMSSMMSSSMSAXMAXMAMAASXSAMSAMXMASXSMSMSSSSMASMMAMXMMSAMAMMSSMAMMMMXAMSMXAAAASAAAAAMSSSMM
AAAAXSSMXSSMMSMSSSMSSSMSAXMSSMSMSMASASAMXAMAASXMASMSMMAAAXAXAAMMMMSMMAXMSMAMAXMASAMXSAMAXMAMXAMASAMMSAMXSASASMAMXXAAXXMMXXSMMXSAMXMSSXMAMXAS
MMSMMMMMMMAAXMAAAAXAXXAMXMXMAMXAXMMMMMMMMMMSMAAMAXMAAMASXMASMMMAAXMAXSSMMXSXMMSSMMXMMXMAMAXMXMMXSXMASMMAMMMMXMXSXXMXMMAXMASXSXMMSXMMAXMASMSM
AXAMAAAASMSSMMMMSMMMMMMMASASMMMAMXSAMMSAXSAMXSXMASASXMAAXSXSXASMSSMMMXAXMAMAMAXAAMXAAAMXSSMMAMMMXMMAXXMSSXMSMXSAMSSSMSSSMMSASXMASAMMMMMMMMXM
MSASXMSMSAAAAAAMAXAXAAXXAMXSXMAXSASAMASMSMASAMSSMMAMXMXMASAXMASXAAAXSSMMMAXAMMSSMMMMSXSXAXASMSAMXSMMXXMAAMMAAMMMMAAAAAAXXSMAMXXMSXMAXAAAAXSS
XSMMAAXXMMMMSMSXSSMXSXSMSMXMAMSASASAMASXMMAMXMASASXMMMAXAMMMMMMMSMMMMAMMMXMAMMAMXAAMAASMMSXMASASMMASMMMMSXSAXSASMSXMMMMMXMMMMSMXMXMASXSSXSAA
MXSMMXSXSXXXMAXAAAXXAASAMAXXAMXMMAMMMXMXAMXMXXMSXMAAXSMMMSAMXXAAAXSASAMSASMSMMMSSXSSMMMAASMSMSXMXMAMXAAAXXMAXSAMAMXAXSXMAMAXAAAAXAAXAAXMMAMM
XAXSSMSAMXSXMAMMSAMXMMMAMASMMSSXXXMASASMSSSSMMXXASMAAAAAASAXXSMXSMMAXAMMASAAXAAMMXAXMXMMMSAMXMASXMMSSXMSSXSXMMAMAMSXMSASXSMSSSMMMAXAMXMMMAXX
MSMASAMXMASAMXMXMMMSASMSMAMAAXMASXSXSAXAAAXAASMSAMXMSSSMXSMMMXMAXAMMMSXMAMXMSMSAMAMMSAXXMMXMAMXMSSXAMXMAMXSAASMMSXMXASAMAAAXAXASXSXSXSXSSSSS
AXMAMSMAMASAMSMXAAAMAMAXXMAMXMASMMAXMXMMMSSXMMXAAXXXAXAXAMASAAMASAMAAXAMXSAMXMMAMMMASXSMSMMSXSAMAMMMSXMAMAXXMMXSXAMMAMAMSMMSMSMSAXAAAXAAAAMA
MXMAMXSAMXSAMXSSMMSMSMMMAMXXAAXMSSSMSAXMAMMXSSXSMMMMMSSMXSAMXXMAMASMSMMMXSAXAMXMSAMMSXXAAAAAMSAMAXXAAXSAMMSSMSMSSMXSXMAMAXXAASAMAMXMMMSMMMXX
ASXMAXMMSMMMSAMMXMXXXAXSXMASAXSXMXAAXXSXAAXMAMAXMXXAAXXAXMASXXXMAAAMMAAXXMASAMMXSASMMAMSSSMSXMXSSMMMSMSASAMAAAAXAMAMMXASMSSMSMAMMMAMAXXAMXMM
AMAMMMAAMAAAXAXXMASMXMMMXXXSXSMAMAMAMXMMSSMXMMSMMXSSSMMMMMAMXMSMMXSASMMSSMMAAXSASXMASXMXAXAXMMAXMASXMAMXMASMMMSSMMASASXSAAMXXMXMASASAXXAMXAX
MSMMASMMSSMXSAMMMMAAASAMSAMXMAXAMAXASAAAMXAAXAMAXAXXMAMSAXASAMXASAMXAAAXAAXMMAMASMSAMAXMXMMMMMMSSMMAMXSXSMMASXAAXXSMMXXMMMMMMAMXASXMASMAXSSM
XAXSAMAAAAAMAMXAAXMSMSAMMMSMMMMXXSXMXMMXSSSXSXXXMMSSMSMSASASASXMMASMSSSSSMXXXMMAMMMMSMMXAAAAXAAMAASXMXAMXMMAMMSSMMXMSMXMAMSAMXMMXSAMAMMXMAMA
SAXMAMSMSSMXASXSMSXMXSAMXAAAAXMSMMASXSMAXMAMSMMMSXAMAMXMAXAMXMXXMXMAAAAAXXSASXMMXXAAAAAXSSMSSMSSSMMMSMMMAXMAMXAMMAXAAAXAAXMMMAMMXSXMASXMMSSS
MMMSAMXAMXMMXMAXXMXMASXMMSSMMAXSASAMMAMXSASXXAAAAXMXXXMASMXMSAMXMMMMSMMSMMSAMXSAXSMSSMSMXAMMXAMXXAAXAAXSMSSSSMASXSMSMSSMSSSMSMMMAMMAMXAAAAAX
SMXMAXXAMSXSMMAMAMAMMMXSAAXMSMMMAMAMSMMXSAXXSSMMXSXMSSXAXMASAMSMSMSAAXXAXAMAMMMAASAAAXMMSAAAMXMAMMMXSMMSAMXXAXSMAXAAAXAAAAMAAAAMXSXMASMMMMSM
MMMSMMSMMXMAXMASAXMMMSAMMSXMAAAMAMAMASXXMAXAXXXSMSAAXASMMAMXAXAAAAAXMMMMMMSAMXMMMMASAMXASXMASAMSSSSXXAXMAMSMMMAMXMSASMMMMSMSSSMSAMASAMMXAAAA
MAAAAXMAMASMXSAMXSXXSMMXAAASXSMSXSMSASMXMXMMMSMAASAMXMASAMMSSMMSMSMAXAAXAAMXXAXAAMAMXXMASXMXMAMXAASAXSMSXMMASMXMAMMAMXXAAXXMXAXMASAMXSSSMSSS
SMSSMMSAMAXXMMXXMAXXMASMMSMSAAXMASAMXSMXSMMMAAAMAMMMSXMMSAAAAAXMAMXASMXSMASXSSMSSSSMXSAXSASMSSMMMMMSMAMMAMXAMAXMXMXMSSSMMSASMMMSMMXMASAXXAMX
XMAXAMXAMXMSXAASXMMMSAMMMAXMMMMMMMAMMXMAMAAMSMSXSMSASMSAXMMSSMXMASAMXMMXMAXAAAMAAMXMASXMXAMAAXXXXAAXSMMSAAMSSSMSMSAXXAXXAXMAAAXAXMAMMMAMMMSS
XSAMXSXMMSXMMMMXAXAMMMMSSSSXMMXXXSMMASMSSSMMMAMXMAMASXMAXSAMAXSSMMASASMXMASMMMAMMMSMMSAMMSMMMMSASMXAMXAMMXXAAXAMASMSMMMXMXXSSMSXSSMSAMXXXAAM
XMASMAASAMASAMMXMMXSAXSAAAMAMSXMASAMSXAAMMXAMAMAMXMMXXMAMMASAMMAMXXMASAAAAXXXMMMXMXAMSAMAAAAMXMXMASMSMSXSMMMSMSMAMXAAAAAMSMXMXXMMAMXAXXSMMSS
XSAMMSMMASASMSAAXAMSASAMMMMXMAAMAMMMXMMMSXMXMASAMXASXMMSMSAMAMSAMMXMXMMMMSSMMXXXSSSMMSMMSSSMSAMXMMAMXAMAXXMAXAXMAMXXMMXAXMMMSMMXMAMMSMMMAAXX
MSMSXMXXMMMMAMMSMAXMMMAXSAMASXSMMSAAXAXMXXXMSASASXXMAAAAXMASAMSASASXXMAMAMAAAXMAXXAXAMAAAAMXMASAXXMSXSMXMMXMXAAMASXSMSSXMAAAAXMAMAMAXMMSAMSM
AXAXMSAXSAXMAMAXXXMMASXMSASASMXAXXMSSSMMMMXMAMXAAXXSSMMSSMMMAMXMMXAMXMAMAMXMMXSMMSAMMSMMSSMASXSMSMMSAMMXAMAMMMSMASXAAAAASXMSMSSMSSMXSAASASXM
SMSMAMAMSAMSAMXSAMSSMSAMSMMXSMSSMXSAMXAAAXMASXMAMAMAMXXMMASMMSMAMMMAAMAMXSMXMAXAXXAMAAAXMXXXSAMAAMAMAMASMMASASAMMSXMMMSMMAAXXAAXAMMASMMXMMXA
XAMMSMSMMAMSAMAMMMXAXMAMXMXAMXAMMMMASXSSSSSXXMASMSMSAMXXSAMAAMXAMSXSSSMSAAAAMMSMMSXMASXMMAMXMAMSMXAXAMXMXSASXSMSXMAMXMAMSMMMMSSMXSMXSSSMSMSS
MXMMMMAAMSMSXMXSSSSSMSSMMSSMMMMSSXXMXXMAMAMMMSMXAAAAMAMMMASMMXSXSAAMAAAMAMSXSAAAAXXMMMMMMASAMAMAMSMSXMAXXMMSMSXSMSAMXSAMSASXAMXMMAXAMXXAAAAA
XXXMAXMSMXAMXMMMMAAAMXAAAAAASAMAXMMMSMMMMASAAAAMSMSMSAAMXAMXAASXSMSMMMMMMXAAMMSSSMSXAAAXSMXMSMMAXAAAMMSXSAASXMAXAMMSASXMSAMXXMASXMMMXAMMMMMM
MSASMSMMAMXMXMAAMMXMAMSMMSSMMAMAXXMAAAAXSASXSMSMAMMASMSSSSSMMXMASAAAXXXMXMMMMMXAAASXMSMMSAMXAMSSSMSMSAAXMAMSAMMMSXMXMXMMMSMAMXXMAXAXMASAAAXX
MXAXAAAXXAAMAXMMXXSASMXAXXAAXMMMXMMSSSMXMXSAMAMMSSMAMMAAXXXXXAMXMSMSAMXXAMXSASMSMMMMMAMMMAMMAMAXAAMXMMSSMMMSXMAAAAMSAMXAAXMSSXASXMAMXAMXXMSM
SMMMSMXMMMXSAMXSSXAAMASMMSSMMSAXAMXAAAXSXSMMMAMAXXMSMMMSMMASXMMSAAXXASMSSXMSAXAMXAAAMASAMMMXXMAXMMMMXMAAAAAXXAMMSSMAAMSMMSAASXMMSSMSMAXSXSXM
SASAAMSMSAMMMXSAAAMXMAMAAAMAASASMMSXSMMAMMASMXMAXSAXXAAAAXAAAAXMMMXXMSAAAAXMSMSMSSSSSXSXXMAMXMXMSAXMAMXSMMSSSXSXAAMSMMXMAMMMMXMAMMASXXMSXMAS
SAMMMXAAMAMAASMMMXMMMXMMMMSSMMMMMASAMXXMAMAMXSXMXMASXSXSSMMSAMSMSXSAAMMMSMMAASXMAMAAMAMASXMASMAASAMSASXMAXAAXAXMMXMASXXMAXXAMAMSSMAMMSMMASAM
MAMXSMMSMMMXXMAAXAMXMAMMSMAASASAMMMAMAMXSMAMAMASXMAMAXAXXXMXMASAAASMMMXXXAXSMSXMASMMMSMAMXSASMXXMAMSAMMMSMMSSMSASASXMMMMMXXMSASAAMMSAAASAMAM
SAMAMAMAMXSXMSSMXXXAMXSAAMSMSSSMSASAMMMAMXSMXMAMAMMSAMXMMXXMASMAMXMAMXXASXMMXXXMAMAMXXMASXSASAMSSMXMMMAAXXXAAXMAMASASXSSSXXASMMMAMXMXSMMMXSM
SAMMSSSMSMXAAAAASMSXSAMXXMAASAMASASMSSSXSAMXSSMSXMXMASXAAMMSMASMMASXMXXMASXMAXMMSXMMSXMXSAMAMXMAAXXAASMSSMMMSMMAMXMMMAAAAASAMXXMXSXSMXMASAMM
MSAMXAAXSASMMSSMXAAAXASXSSMSMAMXMMMAAAAMMXMAAAASAMXXXMXMSAXXXAMXMXAXXSXXAXMSSSMAAASAMXSAMXMAMXMMSMMXMSAXXXAXAAMXSXSXMMMMMMAMSSMSASAMAMXAMMSS
SXMASXMXMASAAAAMMMMMMMXMAAXMXMMSAXMMMSMAASMMSMMMASMMSMMXMXMMMMSAMMAMXMAMSSMAAAMASXMAMAMASMXMXMXAMXMASMXMMSSSXSAXSASMSSSMXXMXAMAAMMXMSSMXSAAX
SSMASAXMMAMMMXMMAMAXXXAMMMMSAMASAMXXXAXMAXXAXAMSAMXAAMSASAXMAXMXSAMXAMXMAAMMSMMXMMSAMXXAMXAMMXMMSASXSAAMXXAAAMXXMAMAAAAXXXXAMMSMXSMMMAAAMMSS
SAMAXMMSMSSSSSMMMSXMASXSXXMXAMXSMSMMMMXXSXMASAMMXSMXSMSASMSMSSMAAXSSSSXMSSMMAMXAAMMASMMXSSMSSXAXSAMAXMAMAMMMMMSAMMMMMSMMMSASXXAXAMAAAMMMSMAX
SAMAMSAMXASAAAAMMMXAXMAMAMMSMMMSXXAAAXXAAAXAMMSMMAMXMXMXMXMAXAXXMAXAXAXMAMASXSSMSMSMMMSXAXMAXMMMMAMXMXSXASAAXAXMASMAMAXAXMXMXMMMMSSMSSMXAMSS
SXMAXXAXMXMMMMMMAAMMSMXMASAAAXASASXMSSMMMMMMSAAAMAMXMASXSSXSSSXMXMSXMMMMASMMMMAMAAAAAAXMSMMMSMSASAMAMMASASMMMMMSASXMSAMSXMAMXAXSMAMXMAMXMSAA
SMMMSSSMMSXMSSSSMSMASMMSASMSSMASAAXAXXASMSAMMMSSMAAMMAMXXMAMAXMXAXMAASMXMSXAASXMXSSMMXSAXMASAMMAMXXAXSMMMXAXXSAMXSAXMAXAMSAMASMAMAXXMASXXMMS
SAMXAAAAAAAXAXXAAAMAXSAMXSAAAMMMMMSMXSSMASMXAXXXMXSAMASXSMMMSMMSSXSSMMASMMMSMXSMMMAMAXMXMAMMASMSMSSSXAXASMMMXMASASMMSMMAMSASXMXSSMSAMAAXAMXX
SSMMMSSMSSSMMSSMMXMSXMXSXMMMXAMXAXAMAXAMXMAMSMMMSMMXSMSAXXXAXAXXAAXXMXAXAMXMSMASASAMSSSSMAMSAMXXXAAXMASMSAXMSXMMMSAMAMMMMSAMAMXAAMAXMMSSMMSM
SAXXAXAAAXAAXAXMASMMASASMSASMAMSXSAMMSMMSMSMMAMSAAAASAMXMXMAMXAMMMMAAMMSSXMAXMAMMMAMMAMXXAXMMSXXMMMMAMXASAMXAXSAMSXMASAAAMMMAMMMMMAXXXMAXAAX
SAMMSSMSMSSMMMXSAMASAMASASASXSXAMSASAAXAXAAASAMASXMMMAMMMMMASXMSAXMXMMXAMAMAXMSSMSXMMMMSSMXASAMXXAXMSMMMMMAMSMSAXXXSASMMMSMMMMXAAMMXMXSXMASM
SSMAXAXAXXMXXMXMASMMASMMAMMMAMMMXSAMMSMSSXSMMMMMAXMASMMAAAMASAASXSAAXXMASXMXSXMAMMMMSMMMASXMMMMMSXSMAXASASAAMASXMXAMXXXXSXXXAASXMMSAMXXXMXXA
MAMXSMMMAMAAXMASAMMSMMXMMMXMAMAMMMXMAMXAXXXXMAAXXMXXXMSMSSMAMXMSAMMAMXSXMXMASMSMMSMAAAMMAMSSMXAAAXMMAMMSAXAMMAMAASMMMMMMSAMXMMSMAAAAAXMMMSMS
SMMAXAAXASMMMXAXASAAMMAMAMXXASASASMMSSSMXXMASMMSAASMSXSMXAMASMXMAMXMXXSASASXMMASAAMMXSMMXMAXASMSSMXSSSMMMMSMMMMSMMAASXSAMAMAAMXMMMSSMSAAXAAA
AXSXSSMMXXAAAMXMMMMXSSXMAXSSMXXMASXAMMXXMMMAMMAMAXAAAAMMSAMAAAAMSMSXMASAMMMAMXAMMSSMSAMAXSMMMSAMXMASMXMASAXAASAMXMSMMAMXSAMXASAMXXAXMAMSSMSM
MMMMMMMXSSSMMXMASASXMMAMSMXAAXSMMSMSSMMSAXMAXMAMMSMSMSMASXMMMSSXAAXMAXMMMSSSMMXSXMAXAAMMMXXAXMASAMSSXAXMMMXMMMAMXAMAMXMASMSXAMXSMXMASXMMXAAX
XAAAAXXXMAMAAMMSMAMXAXSAXASMMMXAAMMAAAAXXXSSMSMSXAMMMXMXSXXSXAAXMMMMMSASXAAAXXAMAMXMSXMASMMSXSASASAMXXSMASMMSXSASXMAMMMMSMMXXMASXSMMSAAAMSMS
SSSSSMMSMAMMXSXAMAMSMMMASAXSAASMMSSMMMMSMXXMASAMXXMASMXXMMASMXMMXAAXASAMMMSMSMMMSMXAMMMMXAMAMMAMMMAMXMAMAMASMAMAMXMXMSAMMMAMMSAMMMAASMMMAXAX
AMAXMAASXMSMASXXMXMAAXMAMMXMXMAMXAXXAMAAXAAMSMAMMSSXSAMXSSMXMSXSSMMXAMAMAAXAMXAXMASMXMASMSMSSMSMMSSMMAMMSSSMMAMAMAMSASASAMXAAMMSSXMMSXXMASMX
XMMMXMXMAMMMASAMXASMSMMMSAMXMMASMMSSMSSMMMSXMMMMMAAMMMMAMASAXXAAAMSSSSXMSMMSMMASMAMXASAMAXAXXAXMAAAASMSMMMMASMSXSAXMAMASXSMMMSAAMASAMMXMAMXS
SAMSSMSSSMAMASMMSMSAMAMAXXXAAMASAAAAXAMXAXMASASAMAXSAAMMSMSMXSAMXMAAAMAMXMAAASMSMAMXMMMMSMSMMSMMMSXMMAAXMASXMASXMAMMMMAMMXAASMMXSAMAXSXMXSAM
XAMAAXMAXSXXXMAMMXSASAMMSMXMSMAMMASMMSSSXSAAXAMASXXSXSSMMXMMAMMXXMXXMSMMAMSSMMAXXAMAXAXXMAMAAAAMAMAMMSMMSAMAMAMXMAMAXMASXXXMXAAAMASXXSAMAMAX
SMMSSMMSMXSSSSMMSASXMMAMAXAAMMSXSXAXXMAXMXMASMXMMMAXAXMMXAXMASMSSMSSXSAMXMXAAMMMSSSMXAMMMAMMMSSMAMXMXAXXMASMMMSMSAXXXXSXAMSSSMMXSAMMASAMMSSS
AXAXMMAAAMSXMASAMXSMMSMSASMSXAMMMSAMMMAMMAXMAMSXAMXMMSXSMMSSMSMASAAXASMSMSSSMMXMAMAMSMSXSASAXXAMXSMXSSXSMAXAASAMXMSMSMAMSMAAMXMXMASAMSAMAAAM
MMXSMMSMSMMASAMXSASAXAAMXSXXMMXAMMSSXMAMMMXSAMMMXMMAXMMSAMXAXXMAMMMMMMAAAXAMXMAMAMAMAAAXASXMSXMAMAAXXAAXMASXMMMMAMAAAAXAMMMMMXSXMXMMXSMMMMXS
XMASXAAXMASAMXSAMASMSMSMMMMMMMSMSAAMMSASAXAMAAAMXMSMXMAMAMSMMSMMSAMXAMMMMMAMXSMSXSASMMMMMMXMMASAMXXSSMMMMXSXAXASASMSMSSSSXXSXMMSMMMSMSXMXSAX
XMAXXSSXMAMXSMMMMAMMMAMMAMXAAXAXMMMXAXASASXSSMSSMAAMXMMSAMXMAAAXSXSSMSMXXMAMXSXAAAAMXSSXXAXASAMMSSXMASMXMAMMSMMXAMXAXXXAXMXMAMAAMAMAASAMAMMS
SMSSMMXXMAMAMXMASAXXMAMASMSSSMMSXSSMSSMMMAMXXMAAMMMSMAXAAXAMSSSMMXXXMAMMSSMXXMMMSMMMXAMMMMSMMASXAAXAXAXASASAXXSSSMSSSMMSMSASAMXSSSSMSMAMASAS
AAXMASAMXXMASASMSMSSSSSXMAAAMAXMAASAAAAAXMMAMSMSMSAMMSMSMMAMAMXAMXSMSASMMASXAXXAMASXMMSAAAAMMMMMXSAMXXSASAMASMMAAXXXAXAAASASASAAXXMXMAXSASAS
MXMSMMASAAXASXSXMAAAAAAAMMMSMSSMMMSMSSSMSMMMMAAMAMXXAAAAXXAXAXXXMSMAXAMMMAMXXMMMSMMAAXMXSSMSMMAXMXAMAMMXMXMMMAMSMMMSXMSSMSXSAMMAMAMXMAMXAMAM
MAMAXSAMXMMASXMMSMMMMXMXMMXXXMAXAMXAAAAAAAXSMMSMAMSMSMSMMSSXMSMSMMXSSSMMMASXMXAMMASMMMMAXMXAASXSAMAMXXMMSAMMSMMAAAAXXMAMXXAMXMAXXMASMMSMMMAM
SASMMSXAASMAMAAAXASXMSMXXSAMXSAMMSMMMSMSSSMMAMXXXMSAMAAXMAXAAAAAAXSAAAAXSAMMXSXSSMXASAMSSMMSMMASMMSMSSXASASAAMSSSMSMXMSXSMSMMXMAXAMXAAXAXXAM
SASXAMASMAMASXMMSAMAXAAXAMXSXMSMSXMMAXXAAMASAMXSMXMAMSXXMAMMXMXXMMAMSMMMXASXASAMAXSAMAMMAAMMXMMMMMXAMXMXSXMMXMAXMAMASMMASAAMAAMMMSXSMMSMMSSS
MAMAMSAMXXSASXSXMASXSMAMMMMSXSAXXAMMSSMSSMXSASAMAXMMMXXAMASXSSXSAXMXMASXSMMMASASAMAXMASMSMMAAXAAAXMAMMSXMASMSMSSMASMMAMXMMMSSXSSXMASMAMAAAMM
MSMXXMXSXAMXSAMXSXMASMASXSAMXMMXSAMXAAAAAMXXMMMSSXSAMXMSMASXAAAXXMXMSAMXMAAMXSXMXSMXMXSMAMXSMSSXSMSXMAMASMMAAAXSMASXMMMASMMXMAAXMASXMAXMMSSX
SAMSSSMMMMMAMXMAMASAMXASAAMXASXMAXMASXMXSMMXXAAXAASMXAAAMMMMXMMMMAXAMMSAMSXMAXAXXAMSSMXXAMMXAXAXMMMASXSAMAMSMSMXMMSXSXMAMAMAMMMMXXMMSXXAXAXM
MASMAAAAAAAAMAMASXASXMMSMSMXXAMXSASAXAAAMAMSMMSMMMMXSMSSSSSMASXXSMXMMXMAXAAMSSMMXAMAAMXSXSAMAMMMMAXASXMASMMMMAAAXAMMSAMXSAMXSSXAXMMAAMSSMASX
SSMMMMSSSMSASASASAMMMMASAAASMMMAMXMSSMMMMAMSXAXAXMAXAXAAXAASAMSXMXSAAAMSAMXXMAMSSMMSSMMMAAXMSMASMMMAMXSAMMAAXMMMSXMASXMXSXSAAXMASAMMMMAMMXMM
XAAMXXAXAAMXXXMASXXAAASMSMAMASMMMAXMXMAXSMMXMAMMAMXMMMMSMSMMXSASAAXMMMXAXXMSSMMXAAAAAMSMSMMMMMXXAXMMAAMMSSSSXSAMMXMASAMXMAMMMMAXSXSXSMMSSMMM
SSMMSXMMMMMMMMSMMXSMSMMAMXXXAMMSXMMMMSAXSXSAAXMSMMAAXAMAMXAASXMMMSXSASMMMXXAAAXMXMMMSMAAXASXSAMSSXMMMAXSAXAAASAMSAMXSXMAMAMAAMXMXAMAMASAXAMX
MXMASAAAMAAAAAAAMXMAXASAMSSMAXAMAMXAMMMSMASXMXXAAMXSXMSMSSMXAMXMAXASASASASMSSMMXSSMAXXMSMASAMMXAMXXAXAXMAMSMMSAMAAAAMMSASMSXSAASMSMAMSMASMMM
XMMAMXSMSSXMXXSXMXSMSAMASAXSSMSSSXSMSAMXMAMASMSSSMMXAAAAMAMAMSXMASMMXSXMASAMAMXXAAMASASXMAMAMXMMSMMMMXXXMAXXXMAXSSMMSASXSXMAMXMSAMSXSAMMMAAX
MMMMMMAMXMXSSMXAXAXAMASXMMMAXXXAMAMASXSXMASXAAXAAAAXMMMMXAMSXSAMASXMASAMXMMXSMMMSXMASXMAMMSSMXMAXAASMMSXSAXAXSSMAXAXMASXMXMAMMSMXMASMXSMMXMS
ASAMMMAMXMXXAAXAMMSXSXMASXXMASMAMXMAMXSMSXAXMMMXMMMXMXSAMSMXASMMASAMASMMAMAXMAXAAMSMXMSSMAAAMSMXMSMMAAMAMSMSMMMAMSMMMAMASMMAXMAAAMXMXXMASAMX
MSASMSXMASMSSMMXMXAAMMMMXXSAMXSSMXMXSAXMASMMSAMSSMSASASAMXAMAMXMSSMMAMAXAMMXSAMXMXAASMMASMSSMAAAXAMSMMMXMAXMAAAAMXAXMXSAMAXASMMSSXSAMXSASASM
AMAMXAMSXSAAMMAXXXMMMAAXMXMXMMMMAASAMMSMAAXASASXAASAMXSAMMAMSMAMAXAMSSSMSXMASXMXSSMSMAMAMXXXMMSMXAXAXXMAMXMSSMSAMXSAMAMASXMMSAAXXASMXXMASXMA
XMAMMSMMAMMMSMSSMASMSSMMAAMAMAAMMMSASXAMMXMXSMMMMMMXMMSXMSXMASASMMSMMAAAAMXAMXSXMAXXXXMSSSMMSMAXXSMMMMSAXSAMXMXMSAMAMMSAMMAXSMMMMXMASMMMMASM
SSMSAAAXAMXXXXAAMAMMXAMXSMSSSSXSAXSAMXMSSXXAXXAAXMMSSMMXXMAMMMMMAAXAXSMMMSMASASAXXAXXXXXAAXAAMXSXMAXAXMXMXXXAXAXMMMXMMMAMSXMXXXAMAAXMXAXSXMS
AAAMXMSXMSMXMMSMMASXMAMAXAAMMMAMAAMAMAXAAMXMAMXSSMAAAAXXMASXXSSSMSSXMASXAXXMMASAMXMSMSMMXMMSMSAMASAMSMSSMSSSSSMSAXSASASMMSASXSSSMMXMSXSMSAAX
XMXMAXAASAMAMMASXXSMSXMXMMMSAXMMSSSMMXMMAXSXXSAMXMMXMMXSMAAXAAAAXAMAXSAMXMAXMXMMMASAMAASMMAXXMAXAMMXXAMAAAAXAAAMAMSAMAMMXMAXAAMMMSAAAAXAXMMM
MXMASMMMXASAXMXSXAXXXASAMAXMAMXAXXAAAXMXAAMAAMAMMXSAASMMASXMMMSMMMSAMAXSSMSSSMSASXSXSSMMASXMSSMMSSMAMMMMSMSMMMMMSMMAMMXMAMMMMSMSAMMMMXMXMMSM
ASXAMAMAMXMXSMAMMMMSMMMASXXMXAMSSSSMMMMMSXMSMSXMAAMMXMAXAMXSXXAXAXMASMMAXAAXASAMXMSMMMMXAMAXAAXAAAMMSXSXXAXMAAAXAASXMMASXSXXAAXMMSXSMMMAMAAS
SSMMSAMASAAXXMAMAAXXSASMMXXXSMXMAXXAAXMMMAMXAMXMMSXSSSSMASXMAXMSSMSAMXMXMMASMMMXAXXAMAMMASMMMSMMSXMXAAMAMMMXSSXMSXMSASXSAMAMMSSMMSAAAASASXMS
AMAMSXSASMSMMSSMSMSMMXSXAXSMSXAMAMSXMSMASAMSASXSMXAAAMASAMAMXMXAMMMMXXMSASAMXMXXXXXAMASMMMMAAAAXAAMSMMMXMAAXXAMXXMXSXMASXSASMAMXAMSSSMSXSXXX
SSMMXMSAMXMAXAXAMMSXSXMMMMMAMSXMXASAXXMMXAMSAMXAAMMMMXMMMSAMXXMASMASAMXAXMASMSSMAMSAMXMMAASXSSSMSAMXXXSXMMMMMAXMASAMAMMMMSASMAMMXMAXXAMXMMMS
MAMMAMMAMMMSXMMSMASAAMXAAAMSMMXSXASXMASXSSMMAMSMMMAAXXAMXMAMSASMMMAXASMMMSAMXAMMAMASXSXSSMMXAAAXXSAXMAMXXASXMMMSSMASXMXAAMAMMXMMAMXSMMMXSAMA
MSMSASMMMMMMAXAXSAMXMAMXMXMAAMASMMMAMMMAMXAXXXAXMSSSSXMAMSAMXASASMSSMMMXAMASMMSSMSAMMMAAMAAMAMMMMMSMSASAMXMAAXMXMAMMMXMMMMAMMXSAMXMMAXAXSXSM
XAMAMXXMAMASAMSMMXSXXSMSMSSXSMAXAASMMSAAASMMMSASAMAXAAXAMMXMASMMMAXAXAXMXSAMAXXAAMXXAASMSSMSAMXAXAAMAAMASMSSMSMAAAMMXSAAASMMSASASXSSMMMXSAMX
MMASXSMMSMMSAMXMMMMMXMAAAAAAXMXSSMSMASXMMAAMXXSMMMMMSMMMSAMXXXXXMXSMMXSAXMASMMSMMMAXSMMAXMASMSSMMMSMMSMAAAAXAAXSXMSXAXMXMSAAMASAMAMAAXSAMXMX
XXAMAMAAAXXMASMXSAMSMMSMSMMMMXMAXAXMASXMXXAMXMAXAAAAAMXXMMMMMSMXXAMXAMMMMXMAMAXAAMMXMAMMMMAMXAXAMAMXAMMMMMMMSMXMAMXMASMSAMXMMXMMMXSAMXMMSMAM
MMAMASMMXSSXMXAAMSMAAMAMAMXSXXAMMSMMASAMXSSSMMMXSSSMMSMSMMAAAAAMSMMXMSAXXMXAMXSSMXSASXMSMMASMSSSMASMMMAXXXAAAXASAMXSXSAMXSAMXXAXXMAMSMMMAAAA
XSXSMSASAAXXMMMMMMSXMXASAMSAMSXSAXXMASAMAMXAAXXXXAXMXAMAASMMSSXMAAMAMMMSMASXSAMXXAMASXMASXXSAAAMMXMASXSSMSSSSMMSAMXXAXXXMMMMSMSMXMMAMASXSSMS
MXXMAMAMMSMXXAAXXMASMSMSASXAMAAMASAMXSMMAXSSMMXSMAMXSSXSXMMAAAASMSMASAAMAMAMXASAMMSMMXSXSXAMMMXMMAMXMSAAMAMAXAXSXMMXMMMMXMAXAAAMAXXMSAMAAMAX
MMMMAMAMXAMMMSXSASXAXAASXMMMMMMMXMAMAXXSMXXMMMMMMMMMAMMMXXMSMSXMAAMXMXMASXMAMMMAXAAAMASMMMSMSMSSMSAMXXMMMSMMXAMXAXXMXAXAAXMSMMMSXSAMXAMXMMMM
AAAMASASMXSAAAMMAMASXMXMASAXAAAXMSSSMSASXXXAAXAXAAAMMSAMXMXMAMAMSMMSXAXAXMASMSSMMSSSMASAXAMASAAAAXMAMXAMXXAXSSMSSMMAMXMSXMMAMXMAAXXAMXSMXXAA
SSXSAMASAMXMMSSMAMAMXXMSASXSMSXSAAAXAAAMMMSSMSSSSSXSASASAAAMAMAXAAASXSMSMSAXXAASXXAXMXSMMMMAMMMMMMSASMXSASAMXXAAMAMSSMAXASXAXXMXSMMSMAAAMSAS
MAXMXMXMMMXMSAXXXMAXXMAMXMMMXXXMMMSMMMAAXAAAMAAAXXAMASAMXSMSMSXSSMMSAMAXAXAMMSMMSMMXMXSXAXMASXXMAMSASAAMAMSMXMMMSSMAAAMMAMMMMMMMMXXAMMMSASXM
MSMSMXMAXXAXMASMXMSMAASMSSMSASMXSAMAXXXSMMMSMMMMMMSMXMXMXXMAAXXXXMMMAMSMMMSMMXAAXXMAMXMSSSMAAXSASXMMMMMMMMAMAXXXAMMSSSXMAMAMAXMASMSXMMAAXMAX
XAAAAASXMMSSXMAXAAAAXAMAAAXXASAAMASXMSMMASAXAAXAXXAMSAMXMMSMSMMSMSSSXMMAAAMASXMMSAMXSAAAXSMMMMSAXMXAXAAAASASMSMMMSMAMXAXASMSMSMASAMAMMSMMSXM
SMSMSMMAASMMMXAXMMMSSMSMSSMMXMMMSXMMASASAMXSSMSXMXASXXMAMXAXXAAAXAMMMMSSMSSMMSMASMMASXSSSSXXSAMAMXSSMXSSXSXXAAASXAMMSMMSAMMAMXMASXMAMAXAXXSM
XAXAAAMSXMAAMMMSMSAMXAXAAMXXXXXXXXAMAMXMMSMXMAMMSMMMMASXXAMXSSMMMMSAMXAMMXMMAMXASMSMSXMXAMAXMSMASXAAMMMMXXAMSMMMSXSXSAXAAXSSMXMASMSMSMSAMXSX
MMMSMMXMASMMSAAAAMMMMAMMMSXMMMMMMXXMXMXXXAAMMAMAXXAAMXMMSSXXMAAXSXSMSMSSMXMMSXMASAMXMASMSMSMAXSASMMMMAAMAMXMAAAAMMSASMMMSMAXXMASXXAMAAMXMAMX
MAAXASMSAMAMSMMSSXMAMAAMAMAAAAAAAAMSMSAMSSSSMSMMSSMMMSAAAXAMXXSAMXMASAMAAMXAMASAMXMXSAMAXAAMXMMMSAAXSMSMXMASMSMXSAMMMXMSMXMAMSMMMSSSMSMAMASX
SSMSAXMAXSAMXAXMXMSMXMMMAXXMMXXMMMXAAAXMAMXMAXSMAAAAASMMSMSMAXMAMSSMXSMXMXMAXMMMSSXMMSSSXSASXAAASXMMSAMMSAAXAXAAMXMAMXXSAMXMAAAAASMSXAXXSAMM
XMAMXMAXXMASXSMSXMASAMXXSSMSXSSMSMSMMMXMAMMMSMAMSSMMXSXMAAAMAXXSMAXXXMXSXMAMXAMXSAMSAMXXXMAMXSMMSXXXMAMASMSMMMMMSMSASXAMAMAXSSSMXMASMSXXMAXA
MMXMSSMSXSXMAXMMXMASMMSAAAASAMXAAAAXXXMMSMASASAMXAASASMSMSXSMSAMMMAMMMAMAMASXMMMSAMMXSMSSMASAMXSXASXMSMMMAXAXMXAXAAASMSMSMXXAAAMSMSMAMMMSXMS
XSAMXMAAMSAMXMAAXMASAASMXMMMSMMSMSMSAASAASXMMXMASMMMASAAAXAAAMAMAXAAAMASXMASXAAXSAMXAAXMASASASXAMMMAAAXSMASXSAMXSMMAMAAAXAMSMSMMASAMXMAAAASM
SSMSAMXMASXMSSXMXSAMMMSXAXAXXXMAXXAXXSMSXSXXXXMASXSMXMMMSMMMXMASXSMSSSMSMMSSXSMMSAMMMSMSXMXSMMMXXXSMMMSXSMXXMXMMMXXAMSMSMXMXXXMSSSXSSSMMSSMA"""

print(
    find_xmas(input)
)
