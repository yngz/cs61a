(define-macro (def func bindings body)
    		  `(define ,func (lambda ,bindings ,body))
)