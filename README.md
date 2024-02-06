# Health Hack 2024
Team: GEN-DSI

### Context

In line with global ambitions to cap global warming at 1.5C or lower, Singapore has raised its own national climate target to achieve net zero emissions by 2050. On top of that, <a href = 'https://www.straitstimes.com/singapore/new-nus-medicine-centre-aims-to-decarbonise-healthcare-prepare-for-climate-related-health-woes'> the Yong Loo Lin School of Medicine</a> has set up a new centre to focus on decarbonising the healthcare sector.

In the same article, Professor Nick Watts, director of the Centre for Sustainable Medicine, points out the complexity of the issue <b>even for doctors</b>, saying, "healthcare is a tough sector to bring to net zero because each patient will require a different strategy to reduce his carbon footprint". Furthermore, non-medical professionals lack the full scope of knowledge and experience required to suggest possible alterations to medical procedures to lower emissions. 

Thus, for the scope of Health Hack 2024, under the problem of sustainability, we chose to look at other methods to lower emissions. In the course of our research, we discovered that pharmaceutical waste is one of the leading contributors of scope 3 emissions, which brings us to our problem statement.

---
### Problem Statement

How can we help reduce the healthcare carbon footprint through <b>reducing drug wastage</b> in Singapore?

---
### Solution

The app we have created is hosted on Streamlit Cloud and makes use of Streamlit libraries. It consists of four tabs/functions:

|Tab|Function|
|:---|:---|
|<b>Home</b>|Contains a brief summary of the project, as well as a login widget.|
|<b>What Can I Donate?</b>|This is an FAQ page along with a pharmaceutical batch checker. For now the batch checker is a dummy tool, as we don't have access to any kind of national database of pharmaceutical batches.|
|<b>Current Inventory</b>|This allows the user (who must be logged in) to manage their own personal inventory of medication and add/subtract from it.|
|<b>Closest Donation Box</b>|This shows a map of all the medicine donation boxes in Singapore, as well as a widget to input an address or postal code and travel radius to load the closest boxes to the address entered. For the purposes of this demo we used the addresses of all public hospitals and polyclinics in Singapore for the locations of the donation boxes.|

---

### Conclusion

1) Our tool combines information and inventory management, allowing users more ownership over their purchasing and consumption, and increasing their awareness of what and how often they are consuming.
2) Even if they do not donate their unused medication, users become less likely to over-purchase OTC medications
3) This kind of awareness at a layman level should also pave the way to more and better understanding of the need to lower carbon emissions in the healthcare sector in general.

---

### Next steps

Possible further development ideas would be to integrate some kind of reminder system for taking medication at a regular interval that can be set by the user, as well as a one-click method to reduce the appropriate amount from the inventory automatically. An alert to purchase more medication when you're running low could also be implemented, or an alert to donate medication when it's approaching its expiration date. 





