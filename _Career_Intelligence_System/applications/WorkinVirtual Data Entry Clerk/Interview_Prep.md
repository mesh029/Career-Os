# Structured Written Interview — Data Entry Clerk, WorkinVirtual

Invited 5 Oct 2026. Written answers, shared only with the hiring team for this application.

## Before you open the link

- **Check the sender.** The email should come from an `@workinvirtual.com` address, and the link should go to `workinvirtual.com`. Both checks look right here.
- **Sign in with the email you applied with:** aririmeshack@gmail.com.
- **Their "Passport"** is only their private candidate profile. Check what they prefill: titles, dates and tools must match the CV (PATH: HMIS Officer, ICT Associate, ICT Intern).
- **Still no money, ID, bank or M-Pesa details, and no remote-access software.** Hold all of that until a written offer names the employer.
- **Plan for one sitting.** Allow about an hour on a laptop with stable internet. Draft answers in a notes file first so nothing is lost if the page times out.

## How to answer

- **Stay in the data-entry and records register.** Talk about data entry and records, not health informatics, dashboards or SQL pipelines, or you'll read as overqualified and likely to leave.
- **Use STAR, kept short:** situation, task, action, result. Aim for 80–150 words per answer.
- **Use a real number where you can:** 3+ years, ~40% faster reporting, 120+ users supported.
- **Write it yourself.** Use the drafts below as notes, then put them in your own words. Written interviews are often screened for AI-generated text, and a natural voice scores better.

## Likely questions and draft answers

**1. Describe your data entry experience.**
> For over three years at PATH, an international health organisation, I have entered, checked and updated records in databases and spreadsheets: DHIS2, KenyaEMR, Excel, Google Sheets and Kobo. Much of it came from paper forms and field submissions. On one programme I entered field forms into Excel and Kobo trackers, cleaned and reconciled them, and kept hard-copy and digital files organised and backed up until the programme closed. Accuracy and confidentiality are the two things I am measured on.

**2. How do you make sure your data is accurate?**
> I check the source before I enter anything, enter in batches, and then check each batch against the source. I use Excel tools that catch problems early: data validation lists, conditional formatting for blanks and outliers, remove-duplicates, and XLOOKUP to match records against a master list. Before anything is submitted, I run a final check for missing, duplicate and inconsistent records. If something doesn't match, I don't guess; I ask the person who owns the source.

**3. Tell us about a time you found an error. What did you do?**
> Monthly reports were going out with missing and duplicate records, which meant corrections after submission. I built simple validation checks in Excel that flagged missing fields, duplicates and values that did not match before submission. Each flagged record went back to the right team with a clear note, and I tracked it until it was fixed. Errors were caught before submission instead of after, and the time spent on reporting fell by about 40%.

**4. The source data is unclear or missing. What do you do?**
> I don't fill the gap with a guess. I flag the record, note exactly what is missing or unclear, and send it to the person or team who owns the source. Then I track it on a follow-up list until it comes back complete. Meanwhile I continue with the clean records so the backlog doesn't grow. On field programmes I followed up late and incomplete submissions this way until every record was complete.

**5. How do you stay accurate on repetitive, high-volume work?**
> I work in focused blocks with short breaks, because accuracy drops when you rush or get tired. I set up the sheet before I start (validation, consistent formats, frozen headers) so the tool catches slips. I check a sample of my own entries at the end of each block. I supported 120+ users at PATH with every request logged accurately, so steady, careful volume is normal for me.

**6. How do you handle confidential information?**
> Most of my records are health data, so confidentiality is part of the job. I only access what the task needs, keep files in approved locations with proper access controls, never share passwords or send records over personal channels, lock my screen, and follow the organisation's data-handling procedures. I would apply the same rules to any client's data.

**7. Which Excel / Google Sheets functions do you use?**
> XLOOKUP and VLOOKUP, IF and IFS, COUNTIF and SUMIF for checks, TRIM, PROPER and TEXT for cleaning, data validation drop-downs, conditional formatting, remove-duplicates, filters and sorting, pivot tables for summaries, and Power Query for repeated cleaning jobs. In Google Sheets I use the same functions plus shared, protected ranges for team work.

**8. Availability and time zone.**
> I am in Kenya (EAT, UTC+3). I can work 4 PM to midnight EAT, which is 9 AM to 5 PM in New York until 1 November. After the US clock change I'll work 5 PM to 1 AM EAT so the overlap stays the same.

*(Change this if your real hours differ. If you take Seamless Assist too, don't double-book the same evening hours.)*

**9. Internet, power and equipment.**
> I have my own laptop and stable home internet, with a mobile data connection as backup. If the power goes out, my laptop battery and phone hotspot keep me working, and I tell the team straight away if anything affects my hours.

*(Only claim a UPS or a second connection if you really have them.)*

**10. Why this role / why remote data entry?**
> I like work where accuracy is visible and matters. I have done this kind of careful records work for three years, and I'm good at it. Remote work lets me give a US team reliable, focused hours from Kenya, with the same care I give health data.

**11. Typing speed.**
Take a free test today (for example typing.com or 10fastfingers) and quote your **real** number with accuracy, e.g. "about 50 WPM at 98% accuracy." Never inflate it; they often test it afterwards.

**12. Expected rate.**
> USD 20 per hour, within the advertised range.

## Technical questions: Excel, Google Sheets and data handling

**1. How do you find and remove duplicate records?**
> First I highlight them so I can review before deleting: Conditional Formatting > Highlight Cells Rules > Duplicate Values, or a helper column with `=COUNTIF($A$2:$A$1000,A2)>1`. I check whether they are true duplicates or two different people with the same name, using a second field like phone or ID. Then I use Data > Remove Duplicates on the right columns. In Google Sheets it's Data > Data cleanup > Remove duplicates, or `=UNIQUE()`. I keep a copy of the original first.

**2. What is the difference between VLOOKUP and XLOOKUP?**
> Both find a value in one list and return matching information from another. VLOOKUP only looks to the right and needs a column number, and you must set the last argument to FALSE for an exact match. XLOOKUP can look left or right, uses exact match by default, and has a built-in "not found" value: `=XLOOKUP(A2, Master!A:A, Master!C:C, "Not found")`. I use XLOOKUP when it's available; it's harder to break when columns move.

**3. How do you stop people entering wrong data in a sheet?**
> Data validation. I add drop-down lists for fixed choices such as status or county, set date and number ranges, and limit text length for things like IDs. I add an input message so the user knows the rule, and an error alert that blocks invalid entries. Excel and Google Sheets both have this under Data.

**4. A column of names has extra spaces and mixed capitals. How do you clean it?**
> `=TRIM(A2)` removes extra spaces and `=PROPER(A2)` fixes the capitals, or `=PROPER(TRIM(A2))` together. Data copied from websites sometimes has non-breaking spaces that TRIM misses, so I use `=SUBSTITUTE(A2,CHAR(160)," ")` first. Then I paste the result back as values. I still scan names like "McDonald" or "O'Brien", because PROPER can get them wrong.

**5. Phone numbers or IDs lose their leading zeros. Why, and how do you fix it?**
> Excel treats them as numbers and drops the zero. I format the column as Text before entering or importing. When importing a CSV, I use Data > From Text/CSV and set that column to Text. For a single entry, an apostrophe before the number keeps it as text. Phone numbers, IDs and postcodes should always be text, because you never do maths on them.

**6. The dates in a file are mixed up (some 03/04/2026, some 4 March 2026). What do you do?**
> First I confirm which format the source uses. A US client writes month/day/year and Kenya writes day/month/year, so 03/04 can mean 4 March or 3 April. I convert everything to one real date format using Text to Columns with the right date order, or DATEVALUE. Then I display them in an unambiguous format like 04-Mar-2026, and I check any dates that look wrong, such as future dates or a day above 12 in the month position.

**7. How do you split a full name into first and last name?**
> Data > Text to Columns with space as the delimiter, or Flash Fill: type the first example and press Ctrl+E. In newer Excel, `=TEXTSPLIT(A2," ")`. To join them back: `=A2&" "&B2` or `=TEXTJOIN(" ",TRUE,A2:B2)`. I watch out for middle names and two-word surnames.

**8. How do you quickly find blank or missing fields?**
> Filter the column for (Blanks), use conditional formatting to colour empty cells, or count them with `=COUNTBLANK(A2:A1000)`. For a whole record, `=COUNTA(A2:H2)` shows how many fields are filled in. Every missing record goes on a follow-up list.

**9. How do you check that a large batch was entered correctly?**
> I compare control totals: the number of records and any key sums in my sheet must match the source. I then spot-check a sample of entries against the source documents, plus any records flagged by my validation or duplicate checks. For critical data, a second person re-enters or checks a sample.

**10. What does IFERROR do?**
> It shows a clean value instead of an error like #N/A when a formula fails. For example, `=IFERROR(VLOOKUP(A2,Master!A:C,3,FALSE),"Check")` shows "Check" so I can review that record instead of the sheet filling with errors. I don't use it to hide problems; it flags them clearly.

**11. When would you use a pivot table?**
> To summarise a large list quickly: records per county, totals per month, counts by status. Insert > PivotTable, then drag fields into Rows, Columns and Values. I also use them as a check, because a count that looks wrong in a pivot often reveals a duplicate or a typo in a category, like "Nairobi" and "Nairobi " showing as two groups.

**12. How do you count records that meet a condition?**
> `=COUNTIF(C:C,"Complete")` for one condition, `=COUNTIFS(C:C,"Complete",D:D,"Kisumu")` for several. `SUMIF` and `SUMIFS` work the same way for totals.

**13. Some numbers will not add up and show a small green triangle. What is wrong?**
> They are stored as text. I select them and use the warning menu > Convert to Number, or Data > Text to Columns > Finish, or `=VALUE(A2)`. Then I check the SUM again.

**14. Which keyboard shortcuts do you use to work faster?**
> Ctrl+Arrow to jump to the edge of data, Ctrl+Shift+Arrow to select it, Ctrl+D to fill down, Ctrl+; for today's date, F2 to edit a cell, Ctrl+H to find and replace, Ctrl+Shift+L for filters, Ctrl+T to turn a range into a table, Ctrl+E for Flash Fill, Alt+Enter for a new line inside a cell, and Ctrl+Z to undo.

**15. How do you keep a shared sheet safe from accidental changes?**
> In Excel I lock formula and header cells and use Review > Protect Sheet, leaving only the entry cells editable. In Google Sheets I use protected ranges and share with the lowest access needed (viewer or commenter where possible). File > Version history lets me restore an earlier version if something goes wrong.

**16. Why use an Excel Table (Ctrl+T) instead of a plain range?**
> A table grows automatically when you add rows, so formulas, formatting, filters and pivot sources keep up. It has banded rows that make entry easier to read, and formulas use clear column names instead of cell addresses.

## Data entry scenarios

**17. You are entering from scanned or handwritten forms and one entry is unreadable.**
> I don't guess. I zoom in and compare the handwriting with other entries on the same form. If it's still unclear, I mark the field as "query" with a note (form number, field, what I can read), send it to the person responsible, and track it until answered. I continue with the clear records.

**18. You notice you entered 50 records with the wrong format yesterday.**
> I report it straight away; hiding it makes it worse. I identify exactly which records are affected, fix them (with a formula or find and replace if the pattern is consistent, manually if not), verify the fix against the source, and explain what I changed and how I'll prevent it, for example by adding validation to that column.

**19. You have a deadline and 2,000 records. How do you plan it?**
> I check the source and template first so I don't redo work. I split the work into batches with a daily target, leave time at the end for checks, and set up validation and formats before I start. If the target looks at risk, I tell my supervisor early, not on the deadline day.

**20. How do you name and organise files?**
> One clear pattern, for example `ClientName_Batch03_2026-10-05.xlsx`, with dates written year-month-day so files sort correctly. Approved folders only, no "final_final2" versions, original source files kept separate from working files, and regular backups.

**21. Have you entered data into a CRM or web system?**
> Yes. At PATH I worked in Salesforce on the user side, resolving tickets on logins, access, forms and reports. I log every request in Freshdesk and Zoho Desk, and I enter health data in DHIS2 and KenyaEMR. The habits are the same in any system: complete every required field, use the agreed formats, search before creating a record so there are no duplicates, and keep notes clear for the next person.

## After submitting

- Note the date in the tracker.
- **Possible next steps:** a typing or Excel test, a short video call, or a client interview.
- **Questions to ask at offer stage:** who the client is, contract type, payment method and frequency (Payoneer, Wise or bank), working hours, and any equipment or software requirements.
