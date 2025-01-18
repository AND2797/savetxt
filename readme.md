save some text (usually URLs) with associated tags

the most common way i use it (and the intended purpose for myself)

```bash
open $(savetxt cat links | fzf | awk '{print $3}')
```
