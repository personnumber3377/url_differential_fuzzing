import json
import subprocess
import validators

import sys

import atheris

with atheris.instrument_imports():
    import urllib.parse

'''




import sys

import atheris

with atheris.instrument_imports():
    import fuzzers


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    choice = fdp.ConsumeIntInRange(0, len(fuzzers.tests) - 1)
    func, data_type = fuzzers.tests[choice]

    if data_type == str:
        data = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    elif data_type == bytes:
        data = fdp.ConsumeBytes(sys.maxsize)
    elif data_type == int:
        data = fdp.ConsumeInt(sys.maxsize)

    try:
        func(data)
    except Exception:
        print(func, data_type, repr(data))
        raise


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()



return {
    "valid": True,
    "scheme": parsed.scheme,
    "username": parsed.username,
    "password": parsed.password,
    "host": parsed.hostname,
    "port": parsed.port,
    "path": parsed.path,
    "query": parsed.query,
    "fragment": parsed.fragment,
}'''


'''

def parse_url_python(url):
    url = urllib.parse.unquote(url)
    print("url: "+str(url))
    """Parses a URL using Python's standard library."""
    try:
        #if validators.url(url) == True:
        #    return {'valid': True}
        #return {'valid': False}
        res = urllib.parse.urlparse(url)
        if not res.scheme:

            return {"valid": False}
        
        if res.port > 65535 or res.port < 1:
            return {"valid": False}

        return {"valid": True}
        #parsed = urllib.parse.urlparse(url)


    except Exception:
        return {"valid": False}
'''


def parse_url_python(url):

    try:
        parsed = urllib.parse.urlsplit(url)  # Use urlsplit() to avoid strict validation

        # If the scheme is missing, we consider it invalid
        if not parsed.scheme:
            return {"valid": False}

        # Manually extract host and port (since urlsplit() does not validate them)
        netloc_parts = parsed.netloc.split(":")
        host = netloc_parts[0]
        port = None
        if len(netloc_parts) > 1:
            try:
                port = int(netloc_parts[1])  # Convert to int
                if res.port > 65535 or res.port < 1:
                    return {"valid": False}
            except ValueError:
                port = None  # Ignore invalid ports

        # Decode path, query, and fragment (including `../`)
        decoded_path = urllib.parse.unquote(parsed.path)
        decoded_query = urllib.parse.unquote(parsed.query)
        decoded_fragment = urllib.parse.unquote(parsed.fragment)
        return {"valid": True}

    except Exception:
        return {"valid": False}


def parse_url_rust(url):
    """Parses a URL using the precompiled Rust binary."""
    result = subprocess.run(["./url_parse", url], capture_output=True, text=True)
    try:
        return json.loads(result.stdout.strip())
    except json.JSONDecodeError:
        return {"valid": False}

def compare_parsers(url):
    """Compares Rust and Python URL parsing results."""
    rust_parsed = parse_url_rust(url)
    python_parsed = parse_url_python(url)

    # Report mismatches
    mismatches = []
    #for key in rust_parsed.keys():
    #    if rust_parsed.get(key) != python_parsed.get(key):
    #        mismatches.append(f"{key}: Rust({rust_parsed[key]}) != Python({python_parsed[key]})")

    if rust_parsed["valid"] != python_parsed["valid"]:
        print(url*100)
        print("python valid:"+str(python_parsed["valid"]))
        print("rust valid:"+str(rust_parsed["valid"]))
        print("Mismatch!")
        

    # Output results
    print(f"Testing URL: {url}")
    print("✅ Match" if not mismatches else f"❌ Mismatch found:\n  " + "\n  ".join(mismatches))
    if mismatches:
        assert False
    print("-" * 50)








'''
# List of test URLs
test_urls = [
    "https://example.com",
    "http://user:pass@example.com:8080/path?query=1#frag",
    "htp://invalid-url.com",  # Invalid scheme
    "https://💩.com",  # Unicode domain
    "https://example.com/%2E%2E/",  # Potential path confusion
    "ftp://localhost:99999999",  # Invalid port
    "http://[::1]:8080",  # IPv6 address
]

# Run comparisons
for url in test_urls:
    compare_parsers(url)
'''

# compare_parsers

def TestOneInput(data):
    try:
        data = data.decode("utf-8")
    except:
        return
    compare_parsers(data)
    return


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()

