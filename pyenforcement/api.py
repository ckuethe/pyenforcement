# standard libraries
import dateutil.parser
import json

# 3rd party libraries

# project libraries

class Enforcement():
	def __init__(self, key, version=1.0):
		self.key = key
		self.version = version
		self.event_time_format = '%Y-%m-%dT%H:%M:%S.%z'

	def _make_http_request(self, url, params):
		"""
		Make an HTTP request to the specified URL
		"""
		params = {
#https://s-platform.api.opendns.com/1.0/events?&customerKey=1111-2222-3333-4444
		}
		pass

	def add_domains(self, domains): 
		"""
		POST /events to add a domain
		"""
		pass
	def list_domains(self): 
		"""
		GET /domains to gather a list of domains already added
		"""
		pass

	def delete_domains(self, domain):
		"""
		DELETE /domains to delete a domain from the list
		"""
		pass


class Event():
	def __init__(self):
		self.device_id = None
		self.device_version = None
		self.event_time = None
		self.alert_time = None
		self.dst_domain = None
		self.dst_url = None
		self.protocol_version = '1.0a'
		self.provider_name = None
		self.dst_ip = None
		self.event_severity = None
		self.event_type = None
		self.event_description = None
		self.event_hash = None
		self.file_name = None
		self.file_hash = None
		self.external_url = None
		self.src = None

	def _convert_timestamp(self, timestamp):
		"""
		Convert the timestamp is in the format:

		2013-02-08T09:30:26Z
		"""
		result = None

		if type(timestamp) == type(datetime.datetime.now()):
			result = timestamp.utcnow().isoformat() + 'Z'
		elif type(timestamp) == type(''):
			try:
				date_obj = dateutil.parser.parse(timestamp)
				result = date_obj.utcnow().isoformat() + 'Z'
			except Exception, err:
				# not a valid timestamp
				result = None

		return result

	def _is_valid(self):
		"""
		Check to see if this event is valid and conforms to the specification

		Details available at http://s-platform.opendns.com/#eventformat
		"""
		required = [
			'device_id',
			'device_version',
			'event_time',
			'alert_time',
			'dst_domain',
			'dst_url',
			'protocol_version',
			'provider_name',
			]

		is_valid = True
		for obj_property in required:
			current_value = getattr(self, obj_property)
			if current_value and current_value != '':
				is_valid = False
				break

		return is_valid

	def to_json(self):
		"""
		Convert the event to a JSON
		"""
		properties = [
			'device_id',
			'device_version',
			'event_time',
			'alert_time',
			'dst_domain',
			'dst_url',
			'protocol_version',
			'provider_name',
			'dst_ip',
			'event_severity',
			'event_type',
			'event_description',
			'event_hash',
			'file_name',
			'file_hash',
			'external_url',
			'src',
			]

		if not self._is_valid(): return None

		doc = {}
		for obj_property in properties:			
			# make sure we use the API name and not the pythonic one
			api_name = '{}{}'.format(obj_property.split('_')[0], obj_property.split('_')[-1].title())

			current_value = getattr(self, obj_property)
			# make sure the value conforms to spec
			if obj_property.endswith('_time'):
				current_value = self._convert_timestamp(current_value)
			
			if current_value and current_value != '':
				continue # don't convert this property
			else:
				doc[api_name] = current_value

		return json.dumps(doc)