        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.content, "html.parser")
        
        print("\nConsolidating all hyperlinks and paragraphs for", self.name)        
        self.paragraph_list = self.soup.findAll('p')
