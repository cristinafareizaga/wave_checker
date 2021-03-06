import argparse
import wave_checker.scrape_url.scrape as sc
import wave_checker.analysis.analysis as an

def analyze_waves(url, no_scrape, orientation):
    csv = sc.scrape_all(url, no_scrape)
    an.analysis_csv(csv, orientation)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Easy way to find the best waves by analyzing windguru')
    parser.add_argument('url', type=str, help='choose windguru url of the desire spot to analyze the waves. i.e https://www.windguru.cz/3645')
    parser.add_argument('--no_scrape', action="store_true", help='select --no_scrape to skip scraping process')
    parser.add_argument('orientation', type=str, help='choose your beach orientation [N,NW,W,SW,S,E,SE,NE]')
    args = parser.parse_args()
    analyze_waves(args.url,args.no_scrape, args.orientation)