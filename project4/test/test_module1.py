from proj.sample_module import add2num

class Testadd2num:

    def test_sum_2pos_num(self):
      assert add2num(6, 7)==13

    def test_sum_1pos_and_1neg_num(self):
      assert add2num(-10, 9)==-1
