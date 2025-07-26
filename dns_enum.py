import dns.resolver

def dns_lookup(domain):
    record_types = ['A', 'MX', 'TXT', 'NS']
    results = {}
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            results[record] = [str(r) for r in answers]
        except:
            results[record] = []
    return results
