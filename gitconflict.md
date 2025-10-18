# Git Merge Conflicts - Complete Guide

## Question: If the changes directly conflicted with each other i.e. another team member made a change to the same line I was editing - what would happen?

---

## ⚠️ When Changes Conflict

### **Scenario:**
```
Remote:  Line 5: "Hello World"  →  "Hello Python"
Local:   Line 5: "Hello World"  →  "Hello GitHub"
```

Both you and your teammate edited the **same line** differently.

---

## 🔴 What Happens During Rebase with Conflicts

### **1. Rebase Starts, Then Stops:**
```bash
$ git pull --rebase origin main

Auto-merging docs/the-soloist.th.md
CONFLICT (content): Merge conflict in docs/the-soloist.th.md
error: could not apply fa419ca... Add explanation image
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply fa419ca... Add explanation image
```

### **2. Git Marks the Conflict in Your File:**
```markdown
# 🏃 นักเดี่ยว

![The Soloist](assets/soloist.jpg)

<<<<<<< HEAD
นักเดี่ยวชอบทำงานคนเดียว (Remote version - from teammate)
=======
The Soloist prefers working alone (Your local version)
>>>>>>> fa419ca (Add explanation image)
```

**What Git Added:**
- `<<<<<<< HEAD` - Start of remote version (what's on GitHub)
- `=======` - Separator
- `>>>>>>> fa419ca` - End of your local version

---

## 🛠️ How to Resolve

### **Option 1: Manual Resolution (Most Common)**

**Step 1:** Open the conflicted file and choose what to keep:

```markdown
# Before (with conflict markers):
<<<<<<< HEAD
นักเดี่ยวชอบทำงานคนเดียว
=======
The Soloist prefers working alone
>>>>>>> fa419ca

# After (you decide):
นักเดี่ยวชอบทำงานคนเดียว
# OR
The Soloist prefers working alone
# OR combine both
นักเดี่ยวชอบทำงานคนเดียว (The Soloist prefers working alone)
```

**Step 2:** Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)

**Step 3:** Mark as resolved:
```bash
git add docs/the-soloist.th.md
```

**Step 4:** Continue the rebase:
```bash
git rebase --continue
```

---

### **Option 2: Keep Their Version**
```bash
git checkout --theirs docs/the-soloist.th.md
git add docs/the-soloist.th.md
git rebase --continue
```

### **Option 3: Keep Your Version**
```bash
git checkout --ours docs/the-soloist.th.md
git add docs/the-soloist.th.md
git rebase --continue
```

### **Option 4: Abort Everything**
```bash
git rebase --abort  # Goes back to before you started
```

---

## 🔍 Real Example from This Project

**If you and a teammate both edited the same line in `the-soloist.th.md`:**

### **Your change:**
```markdown
![Explain](assets/002explain.gif)  
```

### **Teammate's change:**
```markdown
![Explain](assets/003explain.gif)  
```

### **Git would show:**
```markdown
<<<<<<< HEAD
![Explain](assets/003explain.gif)  
=======
![Explain](assets/002explain.gif)  
>>>>>>> fa419ca
```

**You'd need to decide:**
- Keep 002? Keep 003? Use both? Pick a different number?

---

## 📊 Conflict Types

| **Conflict Type** | **Example** | **Difficulty** |
|------------------|-------------|----------------|
| **Same line edited** | Both changed line 5 | ⚠️ Manual choice needed |
| **One deleted, one edited** | You edited, they deleted | ⚠️ Decide keep or delete |
| **Both added different content** | Both added new sections | ⚠️ Merge both or choose |
| **Different files** | You edited A, they edited B | ✅ No conflict! |
| **Different lines same file** | You edited line 5, they edited line 20 | ✅ No conflict! |

---

## 💡 Best Practices to Avoid Conflicts

1. **Pull often** - `git pull --rebase origin main` frequently
2. **Small commits** - Commit and push smaller changes more often
3. **Communicate** - Tell team when working on same files
4. **Feature branches** - Work on separate branches for big changes
5. **Review before pushing** - Check `git status` and `git diff`

---

## 🎯 Summary

**No conflicts (your case):** ✅ Automatic merge - both changes included seamlessly

**With conflicts:** 
1. ⚠️ Git stops and asks you to decide
2. 👀 You manually review and choose
3. ✏️ Edit file to resolve
4. ✅ Mark resolved with `git add`
5. ▶️ Continue with `git rebase --continue`

---

## 🔄 Understanding Rebase

### **Before Rebase:**
```
Remote (origin/main):     A -- B -- C -- D
                           \
Local (main):               \-- X
```
- Remote has commits B, C, D
- You have local commit X

### **After Rebase:**
```
Remote + Local:           A -- B -- C -- D -- X
                                            ↑
                                         (main)
```

### **What Happened:**

1. ✅ **All remote changes are pulled** (commits B, C, D)
2. ✅ **Your local changes are "replayed"** on top (commit X)
3. ✅ **Result:** Linear history with everything included

**Key Point:**
**Yes, both local AND remote changes are in the final version!** Rebase just makes a cleaner, linear history by putting your changes on top instead of creating a merge commit.

Think of it like this:
- 🔄 **Rebase** = "Take my changes and replay them on top of the latest remote"
- 🔀 **Merge** = "Combine both branches with a merge commit"

Both keep all changes, just organized differently!

---

## 🎨 VS Code Conflict Resolution

The good news: **VS Code has great conflict resolution UI** with buttons to:
- ✅ Accept Current Change (your version)
- ✅ Accept Incoming Change (remote version)
- ✅ Accept Both Changes
- ✅ Compare Changes (side-by-side view)

This makes resolving conflicts much easier than manual editing!

---

## 📚 Additional Resources

- [Git Rebase Documentation](https://git-scm.com/docs/git-rebase)
- [Resolving Merge Conflicts](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line)
- [VS Code Git Integration](https://code.visualstudio.com/docs/sourcecontrol/overview)
