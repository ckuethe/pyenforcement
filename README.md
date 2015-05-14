# PyEnforcement

PyEnforcement is a python module for accessing the [OpenDNS Security Platform API](http://s-platform.opendns.com/#overview). This API is provided in the "[Platform](https://www.opendns.com/enterprise-security/threat-enforcement/packages/)" level package.

## Installation

## Usage

The module is very simple to use. But the first step you have to take is to get your customer key from the Umbrella Dashboard. OpenDNS has published instructions on [how to get the key](https://support.opendns.com/entries/67200684?flash_digest=7ab73d9693636fe1ea93141c2e239f6de0a1a193) on their support site.

Once you have the key, the module is as easy as:

```python
import pyenforcement

opendns = pyenforcement.enforcement.Api('___MY_CUSTOMER_KEY___')
current_list = opendns.list_domains()
>>> { 'groogle.com': 123, 'foundthistoday.com': 456, 'badbadstuff.net': 789 }
```

## Methods

The enforcement.Api() class exposes three main methods:

1. .list_domains()
2. .add_events(events)
3. .delete(domain_name_or_id)

Each of these is a direct python implement of the matching API endpoint.

### .list_domains()

This method queries the API to determine what domains you've already set to be blocked. By default it returns the first 200 items on the list but using the parameters [ page, get_all ] you can navigate the list of all the domains you've requested to be blocked for your organization.

Returns a dict of domain:api_id.

```python
import pyenforcement

opendns = pyenforcement.enforcement.Api('___MY_CUSTOMER_KEY___')

current_list = opendns.list_domains()
for domain, api_id in current_list.items():
	print '{}\t{}'.format(domain, api_id)

>>> groogle.com 	123
>>> foundthistoday.com 	456
>>> badbadstuff.net 	789
```

### .add_events(events)

Add an event or list of events to be tracked. The domains implicated in the event (event.dst_domain) will be blocked for your organization.

### .delete(domain_name_or_id)

Delete a domain from your organizations list. A domain name or the API's ID number can be passed to the method.
