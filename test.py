import unittest
import simple_class2
import logging
import sys

def main(out = sys.stderr, verbosity = 2):
		logging.basicConfig(filename='unit_test.log',format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',level=logging.DEBUG)
		loader = unittest.TestLoader()
		suite = loader.loadTestsFromModule(sys.modules[__name__])		
		logging.info(unittest.TextTestRunner(out, verbosity = verbosity).run(suite))		
		

class SimpleTests(unittest.TestCase):
		
	obj = simple_class2.qury_testing()
	#obj.result_Value()

	def testBrand(self):
		try: 							
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_1'),'Unit Test Fail for : Brand')		
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_1'),'Unit Test Fail for : Brand')
			self.assertEqual(True,self.obj.is_title_value('unit_test_1'),'Unit Test Fail for : Brand')
			logging.info("Successfully run test for Brand facet")		
		except:
			logging.warning("Test fail for Brand facet")
		
	def testCustomerRecommended(self):
		try:						
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_2'),'Unit Test Fail for : CustomerRecommended')
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_2'),'Unit Test Fail for : CustomerRecommended')
			self.assertEqual(True,self.obj.is_title_value('unit_test_2'),'Unit Test Fail for : CustomerRecommended')
			logging.info("Successfully run test for CustomerRecommended facet")	
		except:
			logging.warning("Test fail for CustomerRecommended facet")

	def testDeals(self):
		try:			
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_3'),'Unit Test Fail for : Deals') 
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_3'),'Unit Test Fail for : Deals')
			self.assertEqual(True,self.obj.is_title_value('unit_test_3'),'Unit Test Fail for : Deals') 
			logging.info("Successfully run test for Deals facet")	
		except:
			logging.warning("Test fail for testDeals facet")
		
	def testDepartment(self):
		try:			
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_4'),'Unit Test Fail for : Department')		
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_4'),'Unit Test Fail for : Department')
			self.assertEqual(True,self.obj.is_title_value('unit_test_4'),'Unit Test Fail for : Department')
			logging.info("Successfully run test for Department facet")
		except:
			logging.warning("Test fail for Department facet")
		
		
	def testEnvironmental(self):
		try:			
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_5'),'Unit Test Fail for : Environmental') 
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_5'),'Unit Test Fail for : Environmental')
			self.assertEqual(True,self.obj.is_title_value('unit_test_5'),'Unit Test Fail for : Environmental')
			logging.info("Successfully run test for Environmental facet")  	
		except:
			logging.warning("Test fail for Environmental facet")
	
	def testInStoreAvailability(self):
		try:			
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_6'),'Unit Test Fail for : InStoreAvailability') 	
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_6'),'Unit Test Fail for : InStoreAvailability')
			self.assertEqual(True,self.obj.is_title_value('unit_test_6'),'Unit Test Fail for : InStoreAvailability')
			logging.info("Successfully run test for InStoreAvailability facet") 
		except:
			logging.warning("Test fail for InStoreAvailabilityl facet")
		
	def testNewArrivals(self):
		try;			
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_7'),'Unit Test Fail for : NewArrivals')
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_7'),'Unit Test Fail for : NewArrivals')
			self.assertEqual(True,self.obj.is_title_value('unit_test_7'),'Unit Test Fail for : NewArrivals')
			logging.info("Successfully run test for NewArrivals facet")
		except:
			logging.warning("Test fail for NewArrivals facet")
		
	def testRating(self):
		try:		 		
			self.assertEqual(True,self.obj.is_Equal_value('unit_test_8'),'Unit Test Fail for : Rating') 
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_8'),'Unit Test Fail for : Rating') 
			logging.info("Successfully run test for Rating facet")
		except:
			logging.warning("Test fail for Rating facet")
		
	def testBaseproduct(self):
		try:			
			#self.assertEqual(True,self.obj.is_Equal_value('unit_test_9'),'Unit Test Fail for : baseproduct')		
			self.assertTrue(self.obj.is_Num_Doc('unit_test_9'),'Unit Test Fail for : baseproduct')
			logging.info("Successfully run test for Baseproduct facet")
		except:
			logging.warning("Test fail for Baseproduct facet")
		
	def testInStock(self):	
		try:				
			#self.assertEqual(True,self.obj.is_Equal_value('unit_test_10'),'Unit Test Fail for : InStock')
			self.assertEqual(True,self.obj.is_Num_Doc('unit_test_10'),'Unit Test Fail for : InStock')			
			self.assertTrue(self.obj.is_In_Stock(),'Item in Out of Stock')
			logging.info("Successfully run test for InStock facet")
		except:
			logging.warning("Test fail for InStock facet")
		
if __name__ == '__main__':
	with open('testing_results.out', 'a+') as f:	
		main(f)
    #unittest.main()
