# standard libraries
import dateutil.parser
import json
import re
import urllib
import urllib2

# 3rd party libraries

# project libraries

class OpenDnsApiException(Exception): pass

class Enforcement():
	def __init__(self, key, version=1.0):
		self.key = key
		self.version = version
		self.event_time_format = '%Y-%m-%dT%H:%M:%S.%z'
		self.base_url = 'https://s-platform.api.opendns.com/1.0'

	def _get(self, url_relative_path, **kwargs):
		"""
		Make an HTTP GET request to the specified URL
		"""
		params = {
			'customerKey': self.key,
			'limit': 1,
			}
		headers = {
			'Content-Type': 'application/json',
			}

		if kwargs is not None:
			# merge the passed parameters with the default
			for k, v in kwargs.items():	params[k] = v

		query_string = urllib.urlencode(params)
		url = '{}/{}?{}'.format(self.base_url, url_relative_path, query_string)
		response = None
		try:
			response = urllib.urlopen(url)
		except Exception, err:
			raise(OpenDnsApiException('Unsuccessful request to URL [{}]. Threw exception: {}'.format(url, err)))

		results = None
		if response:
			try:
				results = json.load(response)
			except Exception, err:
				raise(OpenDnsApiException('Could not convert the response from URL [{}] to JSON. Threw exception: {}'.format(url, err)))

		return results

	def _post(self, url_relative_path, data, **kwargs):
		"""
		Make an HTTP POST request to the specified URL
		"""
		auth_params = {
			'customerKey': self.key,
			}
		headers = {
			'Content-Type': 'application/json',
			}

		data = {}
		if kwargs is not None:
			# merge the passed parameters with the default
			for k, v in kwargs.items():	data[k] = v

		post_data = urllib.urlencode(data)
		url = '{}/{}?{}'.format(self.base_url, url_relative_path, urllib.urlencode(auth_params))
		response = None
		try:
			req = urllib2.Request(url, post_data)
			response = urllib2.urlopen(req)
		except Exception, err:
			raise(APIException('Unsuccessful request to URL [{}]. Threw exception: {}'.format(url, err)))

		results = None
		if response:
			try:
				results = json.load(response)
			except Exception, err:
				raise(APIException('Could not convert the response from URL [{}] to JSON. Threw exception: {}'.format(url, err)))

		return results


	def add_domains(self, events): 
		"""
		POST /events to add a domain

		events:
			One or more events in the generic event format for the API. Enabled via api.Event()
		"""
		if type(events) != type([]): events = [events]

		data = '['
		for i, event in enumerate(events):
			if i != len(events-1):
				data += '{},\n'.format(event.to_json())
			else:
				data += ']'

		print data

	def list_domains(self, page=1, get_all=False): 
		"""
		GET /domains to gather a list of domains already added
		"""
		# /domains returns calls in pages of 200 domains
		# do we need to get all of the pages?
		if get_all:
			more_pages = True
			while more_pages:
				response = self._get('domains', page=page)
				print response

				# are there more pages to request?
				if response and response['next']:
					page = response['next']
					print "next page: {}".format(page)
				else:
					more_pages = False

		else:
			# get a specific page 
			response = self._get('domains', page=page)
			print response

	def delete_domains(self, domain):
		"""
		DELETE /domains to delete a domain from the list
		"""
		pass