from ..utils import visit, format, dag2dot, dot2svg
import unittest
from fgl import FGL
from fgl.support.exceptions import DSLException
import unittest

# def print(*args, **kwargs):
#     pass

class ParadigmTestCase(unittest.TestCase):
    '''范式
    '''

    def test_0_paradigm_create(self):
        print(FGL().parse("CREATE OR REPLACE PARADIGM test_temp() BEGIN END;")
              ['output'])
        pass

    def test_1_paradigm_show(self):
        print(FGL().parse("SHOW PARADIGMS")['output'])
        print(FGL().parse("SHOW PARADIGM test_temp")['output'])
        # print("AA:", FGL().parse("SHOW PARADIGM attribute_transductive")['output'])
        # import pdb 
        # pdb.set_trace()

    def test_2_paradigm_call(self):
        pass

    def test_3_paradigm_delete(self):
        print(FGL().parse("DELETE PARADIGM test_temp")['output'])
        pass

    def test_4_paradigm_showagain(self):
        print(FGL().parse("SHOW PARADIGMS")['output'])
        print(FGL().parse("SHOW PARADIGM test_temp")['output'])


    def test_5_paradigm_not_define(self):
        try:
            FGL().parse_dag(
                "CALL PARADIGM test_temp_undefine({'did': 'did', 'topo':{'n1':'d1', 'n2':'d2'}}, {'rate':0.8}) AS c;"
            )
        except Exception as e:
            self.assertIsInstance(e, DSLException)
        else:
            raise Exception("not catch DSLException")



class DataModelTestCase(unittest.TestCase):
    '''数据模型
    '''

    def test_0_datamodel_create(self):
        print(FGL().parse("CREATE OR REPLACE DATAMODEL test_temp() BEGIN END;")
              ['output'])
        pass

    def test_1_datamodel_show(self):
        print(FGL().parse("SHOW DATAMODELS")['output'])
        print(FGL().parse("SHOW DATAMODEL test_temp")['output'])

    def test_2_datamodel_call(self):
        pass

    def test_3_datamodel_delete(self):
        print(FGL().parse("DELETE DATAMODEL test_temp")['output'])
        pass

    def test_4_datamodel_showagain(self):
        print(FGL().parse("SHOW DATAMODELS")['output'])
        print(FGL().parse("SHOW DATAMODEL test_temp")['output'])


    def test_5_datamodel_not_define(self):
        try:
            FGL().parse_dag(
                "CALL DATAMODEL test_temp_undefine({'did': 'did', 'topo':{'n1':'d1', 'n2':'d2'}}, {'rate':0.8}) AS c;"
            )
        except Exception as e:
            self.assertIsInstance(e, DSLException)
        else:
            raise Exception("not catch DSLException")
        

class JobTestCase(unittest.TestCase):
    '''自动任务
    '''

    def test_0_job_create(self):
        print(FGL().parse("CREATE OR REPLACE JOB test_temp BEGIN END where aa=3;")
              ['output'])
        pass

    def test_1_job_show(self):
        print(FGL().parse("SHOW JOBS")['output'])
        print(FGL().parse("SHOW JOB test_temp")['output'])

    def test_2_job_call(self):
        pass

    def test_3_job_delete(self):
        print(FGL().parse("DELETE JOB test_temp")['output'])
        pass

    def test_4_job_showagain(self):
        print(FGL().parse("SHOW JOBS")['output'])
        print(FGL().parse("SHOW JOB test_temp")['output'])


    def test_5_job_not_define(self):
        try:
            FGL().parse_dag(
                "CALL JOB test_temp_undefine({'did': 'did', 'topo':{'n1':'d1', 'n2':'d2'}}, {'rate':0.8}) AS c;"
            )
        except Exception as e:
            self.assertIsInstance(e, DSLException)
        else:
            raise Exception("not catch DSLException")
        