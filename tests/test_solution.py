from solution.Solution import Solution
import solution.parser as sp
import pytest
from testfixtures import TempDirectory
import os

@pytest.fixture
def solution_parragh_filepath():
    d = TempDirectory()
    
    content_solution = b"""outputfile for pr02.txt

    0 D:	455.309 Q:	3 W:	7.1095 T:	53.0065	0 (w: 0; b: 85.2408; t: 0; q: 0) 44 (w: 0; b: 89; t: 0; q: 1) 20 (w: 29.7905; b: 131.026; t: 0; q: 2) 92 (w: 0; b: 142.205; t: 43.2055; q: 1) 38 (w: 0; b: 153.316; t: 0; q: 2) 27 (w: 0; b: 167; t: 0; q: 3) 68 (w: 15.4097; b: 195; t: 53.9744; q: 2) 86 (w: 0; b: 209.645; t: 46.3291; q: 1) 30 (w: 21.2879; b: 248; t: 0; q: 2) 75 (w: 0; b: 261.402; t: 84.4021; q: 1) 15 (w: 58.657; b: 334.401; t: 0; q: 2) 78 (w: 0; b: 348; t: 90; q: 1) 1 (w: 0; b: 359.092; t: 0; q: 2) 25 (w: 18.666; b: 390; t: 0; q: 3) 63 (w: 0; b: 405.759; t: 61.3586; q: 2) 4 (w: 0; b: 418.866; t: 0; q: 3) 52 (w: 0; b: 431.388; t: 2.52195; q: 2) 49 (w: 12.5978; b: 459; t: 89.9084; q: 1) 26 (w: 0; b: 473.387; t: 0; q: 2) 73 (w: 0; b: 488.611; t: 88.6115; q: 1) 74 (w: 0; b: 500.733; t: 17.3457; q: 0) 37 (w: 0; b: 512.889; t: 0; q: 1) 85 (w: 0; b: 528.304; t: 5.41463; q: 0) 0 (w: 0; b: 540.55; t: 0; q: 0) 

    1 D:	373.95 Q:	3 W:	4.99494 T:	26.9578	0 (w: 0; b: 130.294; t: 0; q: 0) 32 (w: 0; b: 131.129; t: 0; q: 1) 3 (w: 0; b: 147.789; t: 0; q: 2) 51 (w: 0; b: 160.728; t: 2.93888; q: 1) 48 (w: 0; b: 173; t: 0; q: 2) 80 (w: 0; b: 184.506; t: 43.3773; q: 1) 18 (w: 0.02555; b: 195.577; t: 0; q: 2) 14 (w: 0; b: 205.873; t: 0; q: 3) 96 (w: 0; b: 216.958; t: 33.9584; q: 2) 66 (w: 0; b: 228; t: 22.4226; q: 1) 62 (w: 10.3861; b: 255; t: 39.1268; q: 0) 16 (w: 40.219; b: 307.726; t: 0; q: 1) 64 (w: 0; b: 318; t: 0.27413; q: 0) 5 (w: 49.2683; b: 382.143; t: 0; q: 1) 7 (w: 0; b: 393.097; t: 0; q: 2) 53 (w: 0; b: 414.597; t: 22.4541; q: 1) 33 (w: 0; b: 430; t: 0; q: 2) 55 (w: 0; b: 445.518; t: 42.4212; q: 1) 39 (w: 0; b: 462.033; t: 0; q: 2) 81 (w: 0; b: 481.006; t: 41.0057; q: 1) 87 (w: 0; b: 493.632; t: 21.5985; q: 0) 0 (w: 0; b: 504.244; t: 0; q: 0) 

    2 D:	381.499 Q:	3 W:	24.5507 T:	37.0241	0 (w: 0; b: 54.962; t: 0; q: 0) 12 (w: 0; b: 60.639; t: 0; q: 1) 40 (w: 0; b: 78.7991; t: 0; q: 2) 34 (w: 0; b: 92; t: 0; q: 3) 82 (w: 0; b: 106.008; t: 4.00812; q: 2) 21 (w: 16.6023; b: 134.571; t: 0; q: 3) 88 (w: 0; b: 148.378; t: 59.5793; q: 2) 60 (w: 0; b: 160.639; t: 90; q: 1) 69 (w: 0; b: 172.609; t: 28.0388; q: 0) 17 (w: 228.905; b: 412.506; t: 0; q: 1) 65 (w: 0; b: 426; t: 3.49444; q: 0) 0 (w: 0; b: 436.461; t: 0; q: 0) 

    3 D:	408.096 Q:	4 W:	7.90828 T:	39.385	0 (w: 0; b: 79.9294; t: 0; q: 0) 42 (w: 0; b: 81.7573; t: 0; q: 1) 36 (w: 0; b: 94.0047; t: 0; q: 2) 29 (w: 0; b: 108.805; t: 0; q: 3) 84 (w: 0; b: 121.356; t: 17.3516; q: 2) 43 (w: 0; b: 133.702; t: 0; q: 3) 77 (w: 0; b: 146.43; t: 27.6245; q: 2) 90 (w: 0; b: 156.712; t: 64.9542; q: 1) 31 (w: 0; b: 168; t: 0; q: 2) 79 (w: 0; b: 179.4; t: 1.39989; q: 1) 91 (w: 0; b: 190.812; t: 47.1093; q: 0) 35 (w: 134.262; b: 337; t: 0; q: 1) 28 (w: 23.9033; b: 373; t: 0; q: 2) 46 (w: 0; b: 384.849; t: 0; q: 3) 23 (w: 0; b: 396.296; t: 0; q: 4) 83 (w: 0; b: 407.798; t: 60.7979; q: 3) 71 (w: 0; b: 420.354; t: 14.0575; q: 2) 2 (w: 0; b: 433.872; t: 0; q: 3) 50 (w: 0; b: 447.352; t: 3.48052; q: 2) 76 (w: 0; b: 458.948; t: 75.948; q: 1) 94 (w: 0; b: 475.976; t: 81.1264; q: 0) 0 (w: 0; b: 488.025; t: 0; q: 0) 

    4 D:	368.463 Q:	6 W:	2.75005 T:	44.4871	0 (w: 0; b: 98.2452; t: 0; q: 0) 11 (w: 0; b: 101.021; t: 0; q: 1) 45 (w: 0; b: 112; t: 0; q: 2) 59 (w: 0; b: 124.645; t: 13.6241; q: 1) 19 (w: 10.9422; b: 148.485; t: 0; q: 2) 93 (w: 0; b: 160.122; t: 38.1223; q: 1) 8 (w: 0; b: 177.721; t: 0; q: 2) 13 (w: 0; b: 191.846; t: 0; q: 3) 61 (w: 0; b: 208; t: 6.15444; q: 2) 56 (w: 0; b: 224.492; t: 36.7706; q: 1) 67 (w: 0; b: 235.986; t: 77.5015; q: 0) 24 (w: 55.059; b: 302.402; t: 0; q: 1) 6 (w: 0; b: 314.838; t: 0; q: 2) 10 (w: 0; b: 327.576; t: 0; q: 3) 22 (w: 0; b: 340.907; t: 0; q: 4) 47 (w: 0; b: 352.429; t: 0; q: 5) 9 (w: 0; b: 364.795; t: 0; q: 6) 72 (w: 0; b: 376.554; t: 64.1518; q: 5) 95 (w: 0; b: 387.576; t: 25.1472; q: 4) 57 (w: 0; b: 398.438; t: 23.643; q: 3) 54 (w: 0; b: 409.175; t: 84.337; q: 2) 58 (w: 0; b: 419.931; t: 82.3544; q: 1) 70 (w: 0; b: 431; t: 80.0931; q: 0) 41 (w: 0; b: 441.582; t: 0; q: 1) 89 (w: 0; b: 453.527; t: 1.94537; q: 0) 0 (w: 0; b: 466.708; t: 0; q: 0) 

    cost: 301.336
    total duration: 1987.32
    total waiting time: 725.982 average: 7.56231
    total transit time: 1965.46 average: 40.9472
    
    """
    filename = 'pr02_result.txt'
    d.write(filename, content_solution)

    filepath = os.path.join(d.path, filename)

    return filepath

def test_get_cleaned_solution_lines_from_filepath(solution_parragh_filepath):
    lines = sp.get_solution_cleaned_lines_from_filepath(solution_parragh_filepath)
    assert len(lines) == 10

def test_get(solution_parragh_filepath):
    lines = sp.get_solution_cleaned_lines_from_filepath(solution_parragh_filepath)
    results = sp.get_solution_overall_results(lines)
    assert (301.336, 1987.32, 725.982, 1965.46, 40.9472, 7.56231) == results 
    
def test_parse_solution_from_file_path(solution_parragh_filepath):
    
    s = sp.parse_solution_from_filepath(solution_parragh_filepath)