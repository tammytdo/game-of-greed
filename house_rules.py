class Points:
    
    def __init__(self, points_earned):
        self.points_earned = points_earned

    def die_scoring(self, die_score_dict):
        die_score_dict = { 'straight': 1500,
                            'three_pairs': 1500,

                            'three_ones': 1000,
                            'four_ones': 2000,
                            'five_ones': 3000,
                            'six_ones': 4000,

                            'three_twos': 200,
                            'four_twos': 400,
                            'five_twos': 800,
                            'six_twos': 1200,
                            
                            'three_threes': 300,
                            'four_threes': 600,
                            'five_threes': 1200,
                            'six_threes': 1800,
                            
                            'three_fours': 400,
                            'four_fours': 800,
                            'five_fours': 1600,
                            'six_fours': 2400,

                            'three_fives': 500,
                            'four_fives': 1000,
                            'five_fives': 2000,
                            'six_fives': 3000,

                            'three_sixes': 600,
                            'four_sixes': 1200,
                            'five_sixes': 2400,
                            'six_sixes': 3600    }

class Calculations(Points):

    def calculate_points(self, die_kept, die_score_dict):
        die_summary = { 1 : die_kept.count('1'),
                        2 : die_kept.count('2'),
                        3 : die_kept.count('3'),
                        4 : die_kept.count('4'),
                        5 : die_kept.count('5'),
                        6 : die_kept.count('6')  }

        points_earned = 0
        pair_counter = 0
        is_a_straight = True

        for value, count in die_summary.items():
            if count != 1:
                is_a_straight = False

            if count == 2:
                pair_counter += 1

        points_earned += die_summary[1] * 100
        points_earned += die_summary[5] * 50
        
        if is_a_straight:
            points_earned += die_score_dict['straight']


        if die_summary[1] == 3:
            print(die_score_dict['three_ones'])
            points_earned += (die_summary[1] * 1000) - 2300
            print(points_earned)
        elif die_summary[1] == 4:
            points_earned += die_score_dict['four_ones']
        elif die_summary[1] == 5:
            points_earned += die_score_dict['five_ones']
        elif die_summary[1] == 6:
            points_earned += die_score_dict['six_ones']

        if die_summary[2] == 3:
            points_earned += die_score_dict['three_twos']
        elif die_summary[2] == 4:
            points_earned += die_score_dict['four_twos']
        elif die_summary[2] == 5:
            points_earned += die_score_dict['five_twos']
        elif die_summary[2] == 6:
            points_earned += die_score_dict['six_twos']

        if die_summary[3] == 3:
            points_earned += die_score_dict['three_threes']
        elif die_summary[3] == 4:
            points_earned += die_score_dict['four_threes']
        elif die_summary[3] == 5:
            points_earned += die_score_dict['five_threes']
        elif die_summary[3] == 6:
            points_earned += die_score_dict['six_threes']

        if die_summary[4] == 3:
            points_earned += die_score_dict['three_fours']
        elif die_summary[4] == 4:
            points_earned += die_score_dict['four_fours']
        elif die_summary[4] == 5:
            points_earned += die_score_dict['five_fours']
        elif die_summary[4] == 6:
            points_earned += die_score_dict['six_fours']

        if die_summary[5] == 3:
            points_earned += die_score_dict['three_fives']
        elif die_summary[5] == 4:
            points_earned += die_score_dict['four_fives']
        elif die_summary[5] == 5:
            points_earned += die_score_dict['five_fives']
        elif die_summary[5] == 6:
            points_earned += die_score_dict['six_fives']

        if die_summary[6] == 3:
            points_earned += die_score_dict['three_sixes']
        elif die_summary[6] == 4:
            points_earned += die_score_dict['four_sixes']
        elif die_summary[6] == 5:
            points_earned += die_score_dict['five_sixes']
        elif die_summary[6] == 6:
            points_earned += die_score_dict['six_sixes']

        if pair_counter == 3:
            points_earned += 1500

        else:
            points_earned += 0

        return points_earned 