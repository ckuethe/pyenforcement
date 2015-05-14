# PyEnforcement

PyEnforcement is a python module for accessing the [OpenDNS Security Platform API](http://s-platform.opendns.com/#overview). This API is provided in the "[Platform](https://www.opendns.com/enterprise-security/threat-enforcement/packages/)" level package.

## Installation

## Usage

The module is very simple to use. But the first step you have to take is to get your customer key from the Umbrella Dashboard. OpenDNS has published instructions on [how to get the key](https://support.opendns.com/entries/67200684?flash_digest=7ab73d9693636fe1ea93141c2e239f6de0a1a193) on their support site.

Once you have the key, the module is as easy as:

```
import pyenforcement

opendns = pyenforcement.enforcement.Api('___MY_CUSTOMER_KEY___')
currently_blocked_domains = opendns.list_domains()
>>> ['groogle.com', 'foundthistoday.com', 'badbadstuff.net']
```

## Methods

The enforcement.Api() class exposes three main methods:

1. .list_domains()
2. .add_events(events)
3. .delete(domain_name_or_id)

Each of these is a direct python implement of the matching API endpoint.

### .list_domains()
### .add_events(events)
### .delete(domain_name_or_id)
