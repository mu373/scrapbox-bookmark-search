# scrapbox-search
Open bookmark URL you have saved in Scrapbox, directly from Alfred

## Scripts
- `search.py`
	- Searches for Scrapbox pages by query
	- Returns search results as JSON for Alfred Script Filter
- `get-bookmark-url.py`
	- Gets the bookmark URL from a specific Scrapbox page
	- The first URL that appears in the page is recognized as bookmark URL
	- Returns URL as text

## Usages
```python
python search.py --token $token --project $project --query "LaTeX"
```
```python
python get-bookmark-url.py --token $token --project $project --title "encoded_page_title"
```
