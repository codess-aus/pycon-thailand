# 🧑‍🏫 The Expert

![The Expert](assets/expert.jpg)

The Expert feels they must know everything - Python, Devops, Infrastructure as Code, Testing, Security - and be able to answer every question on any topic. This mindset can lead to stress and burnout.

ผู้เชี่ยวชาญ – ประเภทนี้เกี่ยวข้องกับความรู้สึกเหมือนเป็นคนหลอกลวง เพราะคุณไม่รู้ทุกสิ่งทุกอย่างเกี่ยวกับเรื่องหรือหัวข้อหนึ่งๆ
---

## 🧠 Why It Happens

Experts often set high standards for themselves and fear being seen as less knowledgeable. They believe they need to know everything before they can contribute or teach others.

> "The more I learn, the more I realize how much I don't know." - Albert Einstein

> "ยิ่งฉันเรียนรู้มากขึ้น ฉันก็ยิ่งตระหนักว่ายังมีอีกมากที่ฉันยังไม่รู้" - อัลเบิร์ต ไอน์สไตน์

With GitHub Copilot if you don't understand how something works, you can just ask it. Depending on which model you choose you will see a more verbose or a more succinct explanation. 

The words you choose in your prompt can also frame what the output will look like - so this explanation is quite verbose, but also there is some assumed level of education in there. I could reframe the question asking it to explain it to me like I'm 5 years old. Or to put it in a fun way. Or - to explain it as if I needed to justify this code block to a senior technical decision maker - so it would give me the right words to defend my code if I need to.

![Explain it to me](assets/ExpertGif.gif)

You can ask your questions in the context of the file you have open, the lines you have highlighted, the whole repository, a specific folder.  

I want all the images in this repository to be styled consistently, responsively and accessibly - so I might ask it to check my code and confirm the way I have written it meets those standards, and if it doesn't - explain to me how I can rewrite it so it does that.

If you are having doubts about your skills as a developer, I strongly recommend you use GitHub Copilot in Ask Mode. That allows you to use it like a coach, a teacher, a trainer - but one that will never get tired of your endless questions. One that is always patient, and can keep going until you feel really confident you understand. 

If you are a more senior dev, you will probably find Edit Mode to be a great enabler. It will help you write the code your were going to write anyway, but faster. It will quickly fill in the boilerplate code for you, acurately predicting what you want from your comments, or even from you starting to type something.  

If you are a Senior Architect - you can see the whole project in your mind (or your docs) and you can acurately describe what you want - or have written the architecture file for the repo and know how to guide an Agent back to the main track when it goes down a rabbit hole, then you will find Agent Mode a tremendous tool... but DO NOT USE THIS if you are a beginner, because you will never learn to code properly, never understand the fundamentals, never have the skills to survive in this field, if you skip straight to Agent Mode and let it code for you.  

![Copilot as a Learning Tool](assets/Copilot%20reading.png)

### Mental Models  

- **Ask Mode** = Conversation. Copilot is your “pair programmer who explains and brainstorms.”  
- **Edit Mode** = Controlled Rewrite. You hand Copilot a patch of code and say “transform this with constraint X.”  
- **Agent Mode** = Delegated Workflow. You define a goal; Copilot plans steps, performs them iteratively, and summarizes progress.

### Capabilities & Constraints  

- **Ask Mode**
    - Pulls lightweight context: the current file, selection, maybe related symbols.  
    - Does NOT alter files directly.  
    - Great for: learning, quick utility snippets, performance/complexity questions, API lookups.  
    - Safe sandbox for exploratory thinking.

- **Edit Mode**  
    - You highlight code (or invoke at file scope), give an imperative instruction: “Optimize this loop,” “Convert to async,” “Add docstrings.”
    - Generates a diff you can accept, partially apply, or reject.
    - Promotes incremental, reviewable change.
    - Encourages clarity: best prompts are specific about constraints (e.g., “Keep public API the same; improve readability; no external deps”).  

- **Agent Mode**
    - Accepts a goal like: “Add JWT auth including middleware, tests, and docs.”
    - Can:
        - Inspect multiple files.
        - Create new modules.  
        - Chain reasoning (“Need config loader → create file → update imports → add tests”).  
    - Sometimes prepare a PR-ready branch (depending on environment).
    - Best when the task has multiple dependent steps or requires repository-wide awareness.
    - Requires trust but verify: always review each step—especially security-sensitive code.  

### Example Scenario (Python)  
Suppose you have this (deliberately naive) function:  

```
def compute_totals(items):
    # items: list of dicts like {"price": 10.0, "qty": 2, "category": "book"}
    subtotal = 0
    cat_map = {}
    for it in items:
        if "price" not in it or "qty" not in it:
            continue
        subtotal += it["price"] * it["qty"]
        c = it.get("category", "uncategorized")
        if c not in cat_map:
            cat_map[c] = 0
        cat_map[c] += it["price"] * it["qty"]
    tax = subtotal * 0.0825
    grand = subtotal + tax
    return {
        "subtotal": subtotal,
        "tax": tax,
        "grand_total": grand,
        "by_category": cat_map
    }
```  

### How You’d Use Each Mode  

1. Ask Mode Prompt: “Explain time complexity of compute_totals and suggest micro-optimizations - don’t change semantics.” Output: Explanation + maybe suggestion to use `defaultdict`, avoid duplicated multiplication, consider Decimal for currency.  

2. Edit Mode Prompt (select the function): “Refactor for readability, use type hints, minimize repeated multiplication, and use Decimal (assume 2-decimal currency).” Possible Result (diff style):  
    ```
    from decimal import Decimal, ROUND_HALF_UP
    from collections import defaultdict
    from typing import List, Dict, Any

    def compute_totals(items: List[Dict[str, Any]]) -> Dict[str, Any]:
        subtotal = Decimal("0.00")
        by_category: Dict[str, Decimal] = defaultdict(lambda: Decimal("0.00"))

        for it in items:
            try:
                price = Decimal(str(it["price"]))
                qty = Decimal(str(it["qty"]))
            except KeyError:
                continue
            line_total = price * qty
            subtotal += line_total
            category = it.get("category", "uncategorized")
            by_category[category] += line_total

        tax_rate = Decimal("0.0825")
        tax = (subtotal * tax_rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        grand = (subtotal + tax).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        return {
            "subtotal": str(subtotal),
            "tax": str(tax),
            "grand_total": str(grand),
            "by_category": {k: str(v) for k, v in by_category.items()}
        }
    ```  
    **Commentary:**

    - Converted to Decimal for currency correctness (float can accumulate rounding error).
    - defaultdict simplifies accumulation.
    - Single computation of line_total.  

3. Agent Mode Prompt: “Introduce a pricing module:”
    - Split compute_totals into: parse_items(), aggregate_by_category(), compute_totals()
    - Add unit tests (pytest) covering edge cases: missing keys, zero qty, large price
    - Add README snippet documenting currency handling
    - Ensure no external dependencies besides stdlib + pytest. The Agent could:
        - Create pricing/__init__.py
        - Add pricing/aggregate.py
        - Write tests in tests/test_pricing.py
        - Update README.md with usage example.

#### Interesting Fact: Multi-step Agents often internally chain multiple “edit-like” operations; conceptually they reuse reasoning loops you’d manually perform.  


## 🌱 To overcome Imposter Syndrome Expert-Style embrace a Growth Mindset  

- **Embrace learning as a journey** - There's always something new to discover
- **Ask questions and seek help** - It's a sign of strength, not weakness
- **Share knowledge with others** - Teaching reinforces your own learning
- **It's okay to say "I don't know"** - Then add "but let's find out together"  

- **โอบรับการเรียนรู้เหมือนการเดินทาง** - มักมีสิ่งใหม่ ๆ ให้ค้นพบเสมอ  
- **ถามคำถามและขอความช่วยเหลือ** - นั่นคือสัญลักษณ์ของความเข้มแข็ง ไม่ใช่ความอ่อนแอ  
- **แบ่งปันความรู้กับผู้อื่น** - การสอนช่วยตอกย้ำการเรียนรู้ของตัวเอง  
- **ไม่เป็นไรที่จะพูดว่า "ฉันไม่รู้"** - แล้วตามด้วย "แต่เรามาค้นหาพร้อมกันเถอะ"  

## ➡️ Next: [The Perfectionist](the-perfectionist.md)
