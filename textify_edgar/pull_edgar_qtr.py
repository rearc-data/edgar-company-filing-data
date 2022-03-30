from datetime import date
import secedgar as sec


# limit which quarterly filings to use
# saves only 10-K and 10-Q filings from quarter
limit_to_10k_10q = lambda f: f.form_type.lower() in ("10-k")
quarterly_filings_limited = sec.filings(start_date=date(2021, 11 ,10),
                                    end_date=date(2021, 11, 11),
                                    user_agent="Dara Kharabi (dara.kharabi@rearc.io)",
                                    entry_filter=limit_to_10k_10q)
quarterly_filings_limited.save("~/Projects/sec_edgar_k_d")