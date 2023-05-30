;; reach-mode.el
;; demo major-mode, reach-mode

;;(define-derived-mode reach-mode fundamental-mode "reach"
(define-derived-mode reach-mode javascript-mode "reach"
  "major mode for reach language code"
  (setq font-lock-defaults '(reach-highlights)))
(provide 'reach-mode)
