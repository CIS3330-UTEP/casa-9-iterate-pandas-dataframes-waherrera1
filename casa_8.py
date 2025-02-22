import pandas as pd
file = open('./big-mac-full-index.csv')
df = pd.read_csv(file)
#df = pd.DataFrame(file)

#In this code I use iterrows and apply to get the difference between dollar and local price for the location on the recorded date
def iterrows():
    for index, row in df.iterrows():
        country_name = row['name']
        price_diff = row['dollar_price'] - row['local_price']
        year = row['date']
        print(f'In {country_name}, the difference between dollar and local price on the date {year} was: ${price_diff}')

def get_pricediff(row):
    return(f'In {row['name']}, the difference between dollar and local price on the date {row['date']} was: ${row['dollar_price'] - row['local_price']}')
           
if __name__ == "__main__":
    print('-----------Using the iterrows method-----------')
    iterrows()
    
    print('-----------Using the apply method-----------')
    result = df.apply(get_pricediff, axis=1)
    for answer in result:
        print(answer)