# Web Search Essentials Cheatsheet

---

## Basic Search Operators

### Exact Match
Use quotes to search for exact phrases.

```
"stack overflow exploit"
```

### Exclude Results
Use minus sign to filter out unwanted terms.

```
JavaScript tutorial -MDN
```

### Wildcard Match
Use asterisk as a wildcard for unknown terms.

```
"* overflow exploit"
```

---

## Advanced Search Operators

### Proximity Operator
Find pages where two terms appear near each other.

```
"artificial intelligence" AROUND(3) "ethics"
```

### Date Range
Search within specific time periods.

```
CVE AROUND(5) linux before:2025-01-01
stack overflow exploit after:2023-01-01 before:2023-12-31
```

### Site-Specific Search
Limit results to a specific domain.

```
JavaScript array methods site:https://developer.mozilla.org/en-US/
```

---

## Location & URL Operators

### Search in URL
Find pages with specific words in the URL.

```
inurl:cve "remote code execution"
```

### Multiple Words in URL
Search for multiple terms in the URL.

```
allinurl:admin dashboard site:gov.in
```

### Search by Country/Domain
Filter by top-level domain.

```
latest movies site:.ru
```

---

## Content-Specific Operators

### Search in Title
Find pages with terms in the title tag.

```
intitle:exploit tutorial
```

### Multiple Words in Title
Search for multiple terms in the title.

```
allintitle:stack overflow exploit
```

### Search in Page Text
Find pages with terms in the body text.

```
intext:exploit intext:CVE
```

### Multiple Words in Text
Search for multiple terms in the page text.

```
allintext:stack overflow exploit tutorial
```

### Search by File Type
Find specific document types.

```
filetype:pdf The Linux Programming Interface
```

---

## Boolean Operators

### OR Operator
Search for one term or another.

```
"stack overflow" OR "buffer overflow"
"stack overflow" | "buffer overflow"
```

### AND Operator
Usually implicit in Google (space = AND).

```
buffer overflow vulnerability
```

### Parentheses
Group terms for complex boolean logic.

```
("stack overflow" OR "buffer overflow") -java
```

---

## Utility Operators

### View Cached Pages
Access cached or deleted pages.

```
cache:github.com
```

### Show Definition
Get quick definitions.

```
define:exploit
```

### Show Related Sites
Find similar websites.

```
related:github.com
```

---

## Social & Real-Time Operators

### Search Social Media
Find social media profiles.

```
@username
```

### Check Weather
Get weather information.

```
weather:bangkok
```

### Search Stocks
Get stock information.

```
stocks:amazon
```

---

## Specialized Search Engines

### Security Research

- **[Shodan](https://www.shodan.io/)** - Search engine for internet-connected devices
- **[Censys](https://search.censys.io/)** - Similar to Shodan, provides detailed device and network intelligence
- **[CVE](https://www.cve.org/)** - Public identifiers for known security vulnerabilities
- **[Exploit Database](https://www.exploit-db.com/)** - Repository of exploits for known vulnerabilities

### Security Tools

- **[VirusTotal](https://www.virustotal.com/gui/home/upload)** - Multi-engine virus scanning service for files
- **[Have I Been Pwned](https://haveibeenpwned.com/)** - Check if your email appears in data breaches

### Code & Development

- **[GitHub](https://github.com/search?q=CVE-2025-55182&type=repositories)** - Search repositories using CVE identifiers and code patterns

---

## Pro Tips

1. **Combine operators** for more precise results: `site:gov.in filetype:pdf "security policy"`
2. **Use quotes liberally** to avoid fuzzy matching on important terms
3. **Leverage AROUND()** to find contextually related information
4. **Remember the minus sign** to exclude irrelevant results quickly
5. **Start broad, then narrow** your search with additional operators

---
