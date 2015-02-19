import json
import requests
import re
import ConfigParser
import sys
import unittest

class qury_testing(object):

	configfile = '/home/sampada/Desktop/Zettata/new_properties_test.cnf'
	config = ConfigParser.ConfigParser()
	config.read(configfile)
	sections =config.sections()
	
	solr_url = ''
	section_one = {}
	section_two = {}
	itemInStock = 0
	num_doc = {}
	is_title = {}
	
	
	def get_Solr_Url(self):
		try:
			section = 'solr'	
			self.solr_url = self.config.get(section, 'solr_url')
		except Exception,e:
			raise e 
	
	def result_Value(self):
		try:
			self.get_Solr_Url()
			for i in range(0,len(self.sections)):
				payload = {}
				result_key = ''
				result_value = ''
				count = 0
				diff_resultvalue = 0			
				options = self.config.options(self.sections[i])	
				flag = False
			
				for option in options:
					if option =='result_key':
						result_key = qury_testing.config.get(self.sections[i], 'result_key')
					elif option =='result_value':			
						result_value = qury_testing.config.get(self.sections[i], 'result_value')
						if re.search(',', result_value):
							result_value = result_value.split(',')
						elif result_value == 'true':
							result_value = bool(result_value)							
					elif option =='q':
						payload[option] = qury_testing.config.get(self.sections[i],option)
					elif option =='fl':
						payload[option] = qury_testing.config.get(self.sections[i],option)
					elif option =='wt':
						payload[option] = qury_testing.config.get(self.sections[i],option)
					elif option =='indent':
						payload[option] = qury_testing.config.get(self.sections[i],option)
					else:
						pass
			
					if len(payload)>2 and (result_key and result_value):
						r = requests.get(self.solr_url, params=payload)
						data = r.json()
						#print data
						self.num_doc[self.sections[i]] = data['response']['numFound']
						l = len(data['response']['docs'])
						count = 0
						for n in range(0,l):
							result_data = data['response']['docs'][n]													
							values = result_data.get(result_key)
							if type(values) == list:
								for value in values:
									if value.istitle():
										flag = True
							elif type(values) == bool:
								pass
							elif result_data.get(result_key).istitle():
								flag = True
							else:
								pass
									
							self.is_title[self.sections[i]] = flag		
								#print values.encode('utf-8').istitle()
							#self.is_title.setdefault(self.sections[i]).append(result_data.get(result_key))
							#self.is_title[self.sections[i]]=result_data.get(result_key)
										
							if result_data.has_key(result_key) and result_key not in('inStock', 'base_product'):
								#print result_data.get(result_key), result_value
												
								if str(result_data.get(result_key)) == result_value:
									count = count + 1
								elif str(result_data.get(result_key)) in result_value:
									count = count + 1						
								elif len(set(result_data.get(result_key)).intersection(set(result_value))) == len(result_data.get(result_key)):
									count = count + 1							
								else:
									diff_resultvalue = diff_resultvalue + 1
							elif result_data.has_key(result_key) and (type(result_value) == bool):
								if result_key == 'inStock':
									in_stock = result_data.get(result_key)									
									if in_stock == True:
										self.itemInStock = self.itemInStock + 1
									else :
										self.itemInStock = self.itemInStock - 1
									
									if result_data.get(result_key) == result_value:						
										count = count + 1
									else:
										diff_resultvalue = diff_resultvalue + 1
									
					
		
				if count > 0 and not(diff_resultvalue):				
					self.section_one[self.sections[i]] = count				
				else:
					self.section_two[self.sections[i]] = diff_resultvalue
		except :
			#raise e
			pass		
	
	def is_Equal_value(self,section):	
		#print self.section_one, self.section_two	
		if self.section_one.has_key(section):			
			return True
		else:			
			return False
	
	def is_title_value(self,section):
		if self.is_title.has_key(section):
			if self.is_title[section]:
				return True
			else :
				return False
	
	def is_Num_Doc(self,section):
		if self.num_doc.has_key(section):
			if self.num_doc[section]: 
				return True
			else:
				return False 
						
	def is_In_Stock(self):					
		if self.itemInStock > 0:
			return True
		else :
			return True
	
obj =qury_testing()
obj.result_Value()


#print obj.test_call('unit_test_1')
#obj.is_title_value()
