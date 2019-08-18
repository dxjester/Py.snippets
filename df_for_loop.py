# append rows in dataframe with a for loop

        index_num = 0
        for item in self.sneaker_list:
            name = item + ': '
            count = self.site_text.count(item)
            day = date.today()
            dtg = datetime.datetime.now()
            category = ''
            if count > 0:
                if item in self.nike_master:
                    self.nike_site_count += count
                    category = 'Nike'
                elif item in self.adidas_master:
                    self.adidas_site_count += count
                    category = 'Adidas'
                elif item in self.new_balance_master:
                    self.new_balance_site_count += count
                    category = 'New Balance'
                elif item in self.puma_master:
                    self.puma_site_count += count
                    category = 'Puma'
                else: 
                    0
            else: 
                if item in self.nike_master:
                    category = 'Nike'
                elif item in self.adidas_master:
                    category = 'Adidas'
                elif item in self.new_balance_master:
                    category = 'New Balance'
                elif item in self.puma_master:
                    category = 'Puma'
                else: 
                    0                
            self.site_df.loc[index_num] = [day, dtg, category, item, count] 
