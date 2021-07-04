import twint

c = twint.Config()
# c.Username = "SyedSaddiq"
c.Search = "#lawan"
# c.To = "SyedSaddiq"
c.Store_csv = True
c.Output = "lawan_hashtag"
c.Since = "2021-07-03"
c.Until = "2021-07-04"

twint.run.Search(c)