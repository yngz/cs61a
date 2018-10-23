(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
)

(define (caddr s)
  'YOUR-CODE-HERE
)

(define (sign x)
  'YOUR-CODE-HERE
)

(define (square x) (* x x))

(define (pow b n)
  'YOUR-CODE-HERE
)

(define (ordered? s)
  'YOUR-CODE-HERE
)

(define (empty? s) (null? s))

(define (add s v)
    'YOUR-CODE-HERE
    )

; Sets as sorted lists
(define (contains? s v)
    'YOUR-CODE-HERE
    )

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (intersect s t)
    'YOUR-CODE-HERE
    )

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    'YOUR-CODE-HERE
    )