# Commit History: /tmp/hyperswitch

**Extracted:** 2025-10-16 11:06:33

**Total Commits:** 1720

**Branch:** all branches

## Summary Statistics

- **Total Insertions:** +1,828,145
- **Total Deletions:** -710,424
- **Total Files Changed:** 46,410
- **Merge Commits:** 0

---

## 1. initial commit

- **Commit:** `430dcd19`
- **Author:** Sampras Lopes <lsampras@protonmail.com>
- **Date:** 2022-11-16T20:37:50+05:30
- **Changes:** 320 files (+64760/-0)

## 2. chore: mirror changes from BitBucket

- **Commit:** `2a2febb0`
- **Author:** Sanchith Hegde <sanchith.hegde@juspay.in>
- **Date:** 2022-11-21T18:47:04+05:30
- **Changes:** 76 files (+2216/-741)

## 3. refactor(redis_interface): separating redis functionality and dependent functionalities outside router crate (#15)

- **Commit:** `10003cd6`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-11-28T11:40:13+05:30
- **Changes:** 22 files (+544/-302)

## 4. refactor(common_utils): move `serde` implementations and date-time utils to `common_utils` crate (#40)

- **Commit:** `863e53c0`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2022-11-30T12:23:04+05:30
- **Changes:** 32 files (+188/-191)

## 5. feat(metrics): add histogram and update opentelemetry dependencies (#32)

- **Commit:** `e65ba2a9`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-01T12:51:31+05:30
- **Changes:** 12 files (+293/-177)

## 6. refactor(RouterData): reorder fields in `RouterData` (#33)

- **Commit:** `32e7d345`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-01T12:54:49+05:30
- **Changes:** 17 files (+111/-122)

## 7. refactor: rename the payment request struct (#48)

- **Commit:** `2a050cc3`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-01T16:30:34+05:30
- **Changes:** 29 files (+437/-711)

## 8. feat: integrate Basilisk locker for storing sensitive data (#34)

- **Commit:** `63652a52`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2022-12-01T17:08:38+05:30
- **Changes:** 20 files (+728/-147)

## 9. feat: add payments session operation (#42)

- **Commit:** `bad0d7ee`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-01T17:13:40+05:30
- **Changes:** 5 files (+242/-3)

## 10. Testability ddd repository (#55)

- **Commit:** `200a085f`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-03T07:18:51+02:00
- **Changes:** 116 files (+3569/-1671)

## 11. feat: Braintree connector integration (#30)

- **Commit:** `e5816760`
- **Author:** Sahebjot singh <sahebjot94@gmail.com>
- **Date:** 2022-12-06T11:55:53+05:30
- **Changes:** 11 files (+782/-1)

## 12. refactor(router): remove `SqlDb`, cleaning (#67)

- **Commit:** `ca91ce31`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-06T07:33:26+01:00
- **Changes:** 25 files (+91/-763)

## 13. refactor: raise appropriate errors instead of `ValidateError` (#71)

- **Commit:** `ab5988e6`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2022-12-06T12:34:07+05:30
- **Changes:** 12 files (+136/-135)

## 14. refactor: extract email validation and PII utils to `common_utils` crate (#72)

- **Commit:** `cbbba379`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2022-12-06T15:19:46+05:30
- **Changes:** 12 files (+202/-156)

## 15. feat(stripe): add setup intent in connector integration (stripe) (#50)

- **Commit:** `c208cd2b`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-07T11:59:40+05:30
- **Changes:** 15 files (+584/-36)

## 16. feat(payment_method_validate): add new operation to payments_operation_core for payment method validation (#53)

- **Commit:** `ff561bdd`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-07T17:23:06+05:30
- **Changes:** 7 files (+380/-15)

## 17. refactor(router): create api models for customers as opposed to using db models (#91)

- **Commit:** `21f3d576`
- **Author:** ItsMeShashank <sattarde9913@gmail.com>
- **Date:** 2022-12-08T13:00:39+05:30
- **Changes:** 21 files (+152/-113)

## 18. feat(routes): add the validation API in payments route (#61)

- **Commit:** `bbe3bd86`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-08T20:06:46+05:30
- **Changes:** 14 files (+287/-93)

## 19. feat(router): dynamically toggle KV for merchant and refactoring around it (#79)

- **Commit:** `f76f3e2f`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-09T13:10:44+05:30
- **Changes:** 38 files (+975/-477)

## 20. refactor(router): separate enums for api (#96)

- **Commit:** `9710af1e`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-09T14:03:43+05:30
- **Changes:** 34 files (+1168/-389)

## 21. customers: Added ephemeral key authentication for customer retrieve (#89)

- **Commit:** `3d7d8917`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2022-12-09T17:58:04+05:30
- **Changes:** 21 files (+214/-41)

## 22. Sessions flow for wallets (#60)

- **Commit:** `0e105db2`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-09T20:58:15+05:30
- **Changes:** 26 files (+378/-162)

## 23. Call multiple connectors (#90)

- **Commit:** `091d5af4`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-09T22:49:55+05:30
- **Changes:** 18 files (+153/-151)

## 24. feat(storage): make amount as an enum (#98)

- **Commit:** `031c073e`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-10T15:05:17+05:30
- **Changes:** 18 files (+190/-95)

## 25. feat(core): add sessions api endpoint (#104)

- **Commit:** `dff8b224`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-10T21:32:03+05:30
- **Changes:** 30 files (+353/-112)

## 26. feat(mandate): added amount based validation and database fields (#99)

- **Commit:** `21a0a3d8`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-11T17:35:43+05:30
- **Changes:** 10 files (+184/-97)

## 27. feat(async_refund): add sync feature to async refund (#93)

- **Commit:** `ea219dc8`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-12T12:46:04+05:30
- **Changes:** 6 files (+178/-66)

## 28. feat(setup_intent): add setup_intent stripe compatibility (#102)

- **Commit:** `01cafe75`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-12T14:34:53+05:30
- **Changes:** 4 files (+558/-2)

## 29. feat(redis_interface): implement functions for `HGET`, `HSET`, `HSETNX` commands (#114)

- **Commit:** `81593e0a`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2022-12-12T15:32:46+05:30
- **Changes:** 8 files (+157/-80)

## 30. refactor(router): move api models into separate crate (#103)

- **Commit:** `d6afbe80`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-12T15:36:45+05:30
- **Changes:** 49 files (+2278/-1869)

## 31. refactor(router): move db models into separate crate and refactoring around it (#125)

- **Commit:** `eb4fe6f4`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-13T12:00:27+05:30
- **Changes:** 106 files (+3993/-3367)

## 32. feat(braintree): Sessions flow for braintree and klarna (#121)

- **Commit:** `7dca6f1e`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-13T12:35:17+05:30
- **Changes:** 19 files (+606/-31)

## 33. refactor(masking): PII improvements (#77)

- **Commit:** `124048ce`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-13T08:50:21+01:00
- **Changes:** 16 files (+188/-162)

## 34. refactor: cleaning, requests and split db files (#75)

- **Commit:** `3acde260`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-13T08:58:48+01:00
- **Changes:** 30 files (+468/-440)

## 35. feat(list_pm): allow client secret authentication for list payment method api (#126)

- **Commit:** `6bf99048`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-13T14:03:33+05:30
- **Changes:** 9 files (+268/-121)

## 36. feat: delete customer data in compliance with GDPR regulations (#64)

- **Commit:** `ae886931`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2022-12-13T19:39:32+05:30
- **Changes:** 12 files (+246/-35)

## 37. refactor: use frunk deriving mechanisms to reduce boilerplate (#137)

- **Commit:** `bcf1dd3a`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-14T11:17:05+01:00
- **Changes:** 9 files (+171/-380)

## 38. feat: Apple pay session flow integrate (#138)

- **Commit:** `8b8ff818`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2022-12-14T17:59:27+05:30
- **Changes:** 29 files (+494/-32)

## 39. refactor(api_models): shrink `Amount` (#140)

- **Commit:** `a4d64eba`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-14T14:03:30+01:00
- **Changes:** 25 files (+149/-114)

## 40. feat(drainer): added drainer which reads from redis stream and executes queries on DB (#142)

- **Commit:** `3bad58b0`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2022-12-16T15:38:03+05:30
- **Changes:** 41 files (+648/-655)

## 41. fix(router): pop bugs in the payments confirm flow (#157)

- **Commit:** `4e433a49`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-16T15:52:20+05:30
- **Changes:** 8 files (+371/-110)

## 42. feat(core): support for gpay session token creation (#152)

- **Commit:** `50706bde`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-19T13:38:03+05:30
- **Changes:** 15 files (+262/-62)

## 43. refactor(storage_models): changed CustomResult in storage_models to StorageResult (#158)

- **Commit:** `8d6d41f2`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2022-12-19T13:41:56+05:30
- **Changes:** 18 files (+104/-185)

## 44. feat(router): add straight-through routing connector selection in payments (#153)

- **Commit:** `d6a3e508`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-19T18:43:04+05:30
- **Changes:** 26 files (+193/-101)

## 45. db: Added Reverse lookup table (#147)

- **Commit:** `87fed685`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2022-12-19T18:50:05+05:30
- **Changes:** 51 files (+937/-201)

## 46. refactor(connectors): remove specific imports from connectors (#161)

- **Commit:** `f3d3abf0`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2022-12-20T13:36:59+05:30
- **Changes:** 9 files (+185/-193)

## 47. refactor(compatibility): remove specific imports (#181)

- **Commit:** `08e9c079`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2022-12-20T18:00:40+05:30
- **Changes:** 12 files (+277/-269)

## 48. refactor(router): make stripe compatibility and certain core routes public (#190)

- **Commit:** `60d1ad52`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-21T14:35:43+05:30
- **Changes:** 9 files (+233/-184)

## 49. refactor: Mandate unification (#191)

- **Commit:** `939827da`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-21T23:27:57+05:30
- **Changes:** 3 files (+153/-144)

## 50. chore(router): clippy::use_self (#203)

- **Commit:** `e044451a`
- **Author:** kos-for-juspay <115210506+kos-for-juspay@users.noreply.github.com>
- **Date:** 2022-12-22T06:50:53+01:00
- **Changes:** 28 files (+338/-382)

## 51. refactor(router): make compatibility module, types and utilities public (#197)

- **Commit:** `8f803ad5`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2022-12-22T11:22:39+05:30
- **Changes:** 9 files (+184/-185)

## 52. refactor: shrink sizes of `VARCHAR` columns and rename some columns (#188)

- **Commit:** `60f076f1`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2022-12-22T12:27:59+05:30
- **Changes:** 26 files (+323/-97)

## 53. fix: fixes to surface level mandate issues (#180)

- **Commit:** `dd7e093f`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-22T12:51:52+05:30
- **Changes:** 16 files (+202/-82)

## 54. fix: resolve `TODO` and `FIXME` in `utils` module (#220)

- **Commit:** `87cedc29`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-23T00:56:09+05:30
- **Changes:** 10 files (+109/-128)

## 55. fix: remove and/or resolve `fixme`s & `todo`s in stripe compatibility (#218)

- **Commit:** `9e0deac3`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2022-12-23T00:56:41+05:30
- **Changes:** 3 files (+138/-136)

## 56. feat(klarna): wallet payment through klarna (#182)

- **Commit:** `06a3c38b`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2022-12-23T00:59:18+05:30
- **Changes:** 14 files (+351/-53)

## 57. refactor(drainer): removed router dependency from drainer (#209)

- **Commit:** `c9276a30`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2022-12-23T15:11:06+05:30
- **Changes:** 11 files (+252/-43)

## 58. feat(connector): Add support for shift4 connector (#205)

- **Commit:** `a996f0d8`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2022-12-23T22:49:33+05:30
- **Changes:** 24 files (+1478/-93)

## 59. chore: add lints in workspace cargo config (#223)

- **Commit:** `e7579a48`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2022-12-24T14:28:03+05:30
- **Changes:** 95 files (+443/-383)

## 60. feat(connector): Cybersource Authorize (#154)

- **Commit:** `61238235`
- **Author:** Sahebjot singh <sahebjot94@gmail.com>
- **Date:** 2022-12-24T15:09:49+05:30
- **Changes:** 26 files (+658/-7)

## 61. fix: resolve `TODO/FIXME` from `router.routes` (#283)

- **Commit:** `09c745f9`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-01-05T11:54:40+05:30
- **Changes:** 3 files (+127/-115)

## 62. fix: check if saved payment method and that in request are for the same customer (#260)

- **Commit:** `3c140678`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-01-05T16:09:10+05:30
- **Changes:** 12 files (+92/-226)

## 63. feat(connectors): implement capture flow for checkout and adyen connectors (#259)

- **Commit:** `adb048db`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2023-01-05T18:25:46+05:30
- **Changes:** 7 files (+369/-18)

## 64. feat: list of refunds (#284)

- **Commit:** `e5330528`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-01-06T14:33:30+05:30
- **Changes:** 7 files (+219/-3)

## 65. chore: rename orca to hyperswitch (#310)

- **Commit:** `c0bb1cc3`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-06T16:40:22+05:30
- **Changes:** 21 files (+121/-119)

## 66. feature(connector): add support for worldpay connector (#272)

- **Commit:** `68f92797`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-01-09T12:56:03+05:30
- **Changes:** 31 files (+2198/-104)

## 67. fix: Add locker_id in merchant account and sbx default locker (#276)

- **Commit:** `c807713a`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-01-09T15:49:17+05:30
- **Changes:** 32 files (+187/-122)

## 68. feat(openapi): automatically generate OpenAPI spec from code (#318)

- **Commit:** `3fe60b5a`
- **Author:** bernard-eugine <114725419+bernard-eugine@users.noreply.github.com>
- **Date:** 2023-01-09T16:09:49+05:30
- **Changes:** 15 files (+1401/-14)

## 69. refactor(router): Refactored Authentication (#327)

- **Commit:** `59573efe`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2023-01-10T15:06:34+05:30
- **Changes:** 17 files (+363/-384)

## 70. refactor: Replace Bach with Application on every naming (#292)

- **Commit:** `3cdf50c9`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-01-10T18:07:32+05:30
- **Changes:** 36 files (+218/-209)

## 71. fix: refund fix with `connector_metadata` (#330)

- **Commit:** `9ad56703`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-01-10T19:24:19+05:30
- **Changes:** 28 files (+163/-91)

## 72. build(deps): update deps (#342)

- **Commit:** `35f6af1a`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-11T13:07:13+05:30
- **Changes:** 15 files (+377/-340)

## 73. feat(connector): add payment create, sync, capture, refund, void, rsync support for globalpay (#322)

- **Commit:** `4fdc7680`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-01-11T19:33:07+05:30
- **Changes:** 26 files (+2550/-163)

## 74. feat: separate olap oltp (#348)

- **Commit:** `8c5eab84`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-01-12T19:49:06+05:30
- **Changes:** 14 files (+213/-74)

## 75. chore: drop `temp_card` table and all associated items (#366)

- **Commit:** `89a1cd08`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-13T14:09:52+05:30
- **Changes:** 22 files (+27/-393)

## 76. feat(connector): add payment create, sync, capture, refund, void, rsync support for PayU (#351)

- **Commit:** `55dba876`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-01-14T13:07:04+05:30
- **Changes:** 14 files (+1504/-9)

## 77. feat(router): add more payment methods to vault (#333)

- **Commit:** `4e00b92d`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-01-14T20:48:45+05:30
- **Changes:** 12 files (+654/-400)

## 78. feat(connector): implement authorize and capture flows for Fiserv (#266)

- **Commit:** `6e15f5a9`
- **Author:** Sahebjot singh <sahebjot94@gmail.com>
- **Date:** 2023-01-15T16:03:06+05:30
- **Changes:** 18 files (+957/-15)

## 79. build(deps): use utoipa crate upstream URL as git dependency (#378)

- **Commit:** `4e9fc244`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-16T14:42:32+05:30
- **Changes:** 5 files (+20/-196)

## 80. feature(connector): add support for worldline connector (#374)

- **Commit:** `a16fc653`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-01-16T18:23:44+05:30
- **Changes:** 15 files (+1390/-1)

## 81. feat(connector_integration): integrate Rapyd connector (#357)

- **Commit:** `006e9a88`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-01-16T23:58:21+05:30
- **Changes:** 15 files (+1306/-2)

## 82. chore: fix typos and introduce ci check (#390)

- **Commit:** `74f6d002`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-17T11:38:47+05:30
- **Changes:** 28 files (+199/-240)

## 83. feat(router): update OLTP/OLAP feature flags to be compatible with each other (#389)

- **Commit:** `a4eaa360`
- **Author:** Sampras Lopes <lsampras@protonmail.com>
- **Date:** 2023-01-17T12:02:58+05:30
- **Changes:** 7 files (+201/-214)

## 84. feat: add docs for PaymentsRequest & PaymentsResponse (#385)

- **Commit:** `72c4b068`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-01-17T12:53:43+05:30
- **Changes:** 7 files (+1108/-23)

## 85. feat(router): add generic merchant static routing config (#362)

- **Commit:** `22f32cd4`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-01-17T13:04:54+05:30
- **Changes:** 22 files (+190/-188)

## 86. feat(connector): add support for capture, void, psync, refund and rsync for cybersource (#381)

- **Commit:** `e1590e7b`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-01-17T13:55:51+05:30
- **Changes:** 9 files (+1053/-218)

## 87. chore: add `.attach_printable` for `InternalServerError` (#368)

- **Commit:** `be9889b4`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-01-17T17:23:57+05:30
- **Changes:** 14 files (+178/-48)

## 88. refactor: move config defaults from TOML files to `Default` trait (#352)

- **Commit:** `beb03840`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-17T19:13:16+05:30
- **Changes:** 20 files (+589/-169)

## 89. fix(router): remove 'connectors_pecking_order' from readmes and tests (#397)

- **Commit:** `cb664856`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-01-17T19:52:53+05:30
- **Changes:** 3 files (+16/-352)

## 90. chore: Added docs for payment connector create (#394)

- **Commit:** `0391f5ef`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-01-17T20:03:16+05:30
- **Changes:** 5 files (+310/-189)

## 91. fix(router): metadata field update in merchant_account and merchant_connector_account (#359)

- **Commit:** `b5ffff30`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-01-18T15:56:09+05:30
- **Changes:** 9 files (+180/-113)

## 92. feature(connector): add capture flow support for worldline (#399)

- **Commit:** `3620c284`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-01-18T16:44:30+05:30
- **Changes:** 11 files (+282/-144)

## 93. feat(router): reuse reqwest clients for requests made to connectors (#413)

- **Commit:** `749c83a8`
- **Author:** Sampras Lopes <lsampras@protonmail.com>
- **Date:** 2023-01-19T15:05:37+05:30
- **Changes:** 3 files (+187/-183)

## 94. doc: Documentation for customer and MCA and Mechant account API (#416)

- **Commit:** `89c75b9c`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-01-19T17:30:45+05:30
- **Changes:** 6 files (+448/-41)

## 95. feat: add connector error (#415)

- **Commit:** `57c46b24`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-01-20T00:23:13+05:30
- **Changes:** 29 files (+305/-163)

## 96. docs: request and response for payments route (#400)

- **Commit:** `8113a57f`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-01-20T01:43:08+05:30
- **Changes:** 6 files (+659/-25)

## 97. refactor(connectors): refactor propagation of validation and not implemented errors (#419)

- **Commit:** `c1de463c`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-01-20T12:07:01+05:30
- **Changes:** 44 files (+534/-295)

## 98. feat(access_token): support creating access token for connectors (#407)

- **Commit:** `30593bd1`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-01-20T16:14:33+05:30
- **Changes:** 38 files (+647/-63)

## 99. fix: add graceful shutdown for consumer & router (#428)

- **Commit:** `25d8ec20`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-01-20T16:25:56+05:30
- **Changes:** 9 files (+160/-76)

## 100. feat(globalpay): implement access token creation (#408)

- **Commit:** `b1b05000`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-01-20T18:25:52+05:30
- **Changes:** 6 files (+213/-18)

## 101. feat(connector): add auth_token_refresh for payu and some quick bug fixes (#426)

- **Commit:** `da6a026e`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-01-21T23:34:44+05:30
- **Changes:** 13 files (+390/-127)

## 102. docs: fix quick start guide and update dashboard link (#454)

- **Commit:** `0ec3aea6`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-01-23T00:16:23+05:30
- **Changes:** 5 files (+81/-290)

## 103. refactor(core): validate payment status using common function (#461)

- **Commit:** `9ae8b4e1`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-01-25T15:29:36+05:30
- **Changes:** 5 files (+197/-175)

## 104. feat(stripe): add support for afterpay clearpay through stripe (#441)

- **Commit:** `351087fc`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-01-25T21:13:21+05:30
- **Changes:** 6 files (+173/-90)

## 105. chore: address Rust 1.67 clippy lints (#465)

- **Commit:** `b5720f1e`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-27T12:29:57+05:30
- **Changes:** 33 files (+107/-123)

## 106. test(stripe): add unit tests for stripe connector (#473)

- **Commit:** `d3ef24e8`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-01-30T15:29:27+05:30
- **Changes:** 4 files (+509/-33)

## 107. doc: update openapi (#453)

- **Commit:** `ec2f4ba2`
- **Author:** bernard-eugine <114725419+bernard-eugine@users.noreply.github.com>
- **Date:** 2023-01-30T16:56:37+05:30
- **Changes:** 40 files (+3339/-308)

## 108. build(deps): update deps (#479)

- **Commit:** `d1ab4623`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-01-31T15:21:34+05:30
- **Changes:** 14 files (+211/-231)

## 109. feat(connector-template): add more default tests for card payment method (#471)

- **Commit:** `010aff5f`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-01-31T16:22:32+05:30
- **Changes:** 2 files (+419/-37)

## 110. test(connector): add and update tests for stripe, cybersource and shift4 connectors (#485)

- **Commit:** `5c3c51fb`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-02-01T14:25:39+05:30
- **Changes:** 23 files (+904/-323)

## 111. feat(config): add fetch endpoint for config table (#481)

- **Commit:** `2735405a`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-02-02T23:47:38+05:30
- **Changes:** 15 files (+216/-6)

## 112. feat: add metrics to drainer (#497)

- **Commit:** `4a820dcd`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-02-06T13:03:53+05:30
- **Changes:** 7 files (+233/-63)

## 113. Rapyd webhook integration (#435)

- **Commit:** `a2921ff8`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-02-06T14:00:30+05:30
- **Changes:** 6 files (+368/-239)

## 114. refactor: AppState trait for utility functions (#499)

- **Commit:** `9381a37f`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-02-06T16:34:29+05:30
- **Changes:** 17 files (+147/-92)

## 115. feat(generics): allow specifying optional offset and order clauses for `generic_filter()` (#502)

- **Commit:** `feb228ce`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-02-06T17:53:37+05:30
- **Changes:** 7 files (+151/-83)

## 116. feat: add timeout for `set` command on hashes and add function to allow retry in database (#509)

- **Commit:** `2e98670a`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-02-07T16:28:39+05:30
- **Changes:** 9 files (+169/-119)

## 117. feat(connector): add afterpay, klarna, affirm support in adyen connector (#516)

- **Commit:** `f6eac13b`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-02-10T02:37:09+05:30
- **Changes:** 7 files (+829/-148)

## 118. feat(router): implement API endpoints for managing API keys (#511)

- **Commit:** `1bdc8955`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-02-10T14:20:57+05:30
- **Changes:** 35 files (+1758/-98)

## 119. fix: throw 500 error when redis goes down (#531)

- **Commit:** `aafb115a`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-02-14T17:13:17+05:30
- **Changes:** 12 files (+169/-86)

## 120. refactor: Throw 500 error on database connection error instead of panic (#527)

- **Commit:** `f1e3bf48`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-02-14T17:14:23+05:30
- **Changes:** 23 files (+117/-98)

## 121. feat(api_models): add error structs (#532)

- **Commit:** `d107b44f`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-02-16T14:49:14+05:30
- **Changes:** 11 files (+288/-55)

## 122. refactor: add payment_issuer and payment_experience in pa (#491)

- **Commit:** `66563595`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-02-19T19:29:22+05:30
- **Changes:** 54 files (+786/-797)

## 123. refactor(redirection): `From` impl for redirection data for ease of use (#613)

- **Commit:** `e8255b4a`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-02-20T16:18:31+05:30
- **Changes:** 5 files (+101/-153)

## 124. feat: applepay payment request object (#519)

- **Commit:** `8ee097ea`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-02-23T14:56:30+05:30
- **Changes:** 8 files (+1001/-372)

## 125. enhance(router/webhooks): expose additional incoming request details to webhooks flow (#637)

- **Commit:** `1b3b7f5b`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-02-24T17:53:16+05:30
- **Changes:** 21 files (+144/-129)

## 126. refactor(connector-template): raise errors instead of using `todo!()` (#620)

- **Commit:** `b1a6be5a`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-02-24T18:15:59+05:30
- **Changes:** 3 files (+113/-125)

## 127. refactor: Pass country and currency as json format in MCA (#523)

- **Commit:** `d27e6be5`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-02-24T19:39:03+05:30
- **Changes:** 5 files (+212/-37)

## 128. refactor(connector): remove `peek()` on PII info (#642)

- **Commit:** `46f77d07`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-02-25T18:22:01+05:30
- **Changes:** 15 files (+113/-110)

## 129. feat(connector): add authorize, capture, void, refund, psync, rsync support for Dlocal connector (#650)

- **Commit:** `7792de55`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-02-25T19:43:40+05:30
- **Changes:** 17 files (+1635/-8)

## 130. chore: merging back release v0.3.0 back to main (#636) (#655)

- **Commit:** `f3224cc4`
- **Author:** Arun Raj M <jarnura47@gmail.com>
- **Date:** 2023-02-26T13:55:17+05:30
- **Changes:** 74 files (+5976/-352)

## 131. feat(stripe): eps, giropay and ideal using stripe (#529)

- **Commit:** `028e1401`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-02-26T21:59:37+05:30
- **Changes:** 92 files (+1530/-1048)

## 132. refactor(pm_list): modify pm list to support new api contract (#657)

- **Commit:** `a2616d87`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-02-27T00:51:29+05:30
- **Changes:** 12 files (+424/-254)

## 133. feat: api contract change for wallet (#628)

- **Commit:** `ff86417e`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-02-27T17:38:40+05:30
- **Changes:** 20 files (+1176/-477)

## 134. feat(pm_list): support for sending bank names (#678)

- **Commit:** `576f8e1f`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-02-28T01:59:06+05:30
- **Changes:** 6 files (+200/-40)

## 135. feat(connector): [Bambora] Add support for cards Authorize, psync, capture, void, refund, Rsync (#677)

- **Commit:** `0de5d441`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-02-28T03:31:50+05:30
- **Changes:** 22 files (+1714/-51)

## 136. feat:H1083-L1-L3-L4-L5 [Payment Authorise and Sync] + [Refunds and Sync] + [Redirection Flow (BNPL)] + [3DS Payment and Sync] for MultiSafePay (#658)

- **Commit:** `79aa8f3d`
- **Author:** rupakrajak <43450369+rupakrajak@users.noreply.github.com>
- **Date:** 2023-02-28T05:04:26+05:30
- **Changes:** 19 files (+1786/-122)

## 137. feat: Add bank redirect mapping to adyen and stripe (#680)

- **Commit:** `e6f627d9`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-02-28T13:23:01+05:30
- **Changes:** 3 files (+313/-29)

## 138. feat(router): added incoming refund webhooks flow (#683)

- **Commit:** `f12abbce`
- **Author:** saiharsha-juspay <99009240+saiharsha-juspay@users.noreply.github.com>
- **Date:** 2023-02-28T19:15:25+05:30
- **Changes:** 12 files (+302/-11)

## 139. docs(openapi): document security schemes (#676)

- **Commit:** `c5fda7ac`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-03-01T11:46:50+05:30
- **Changes:** 12 files (+419/-86)

## 140. feat(router): serve OpenAPI docs at `/docs` (#698)

- **Commit:** `ed2907e1`
- **Author:** bernard-eugine <114725419+bernard-eugine@users.noreply.github.com>
- **Date:** 2023-03-01T23:46:45+05:30
- **Changes:** 12 files (+356/-489)

## 141. refactor(router): remove foreign wrapper type (#616)

- **Commit:** `7bd2008a`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-03-01T23:48:26+05:30
- **Changes:** 11 files (+237/-401)

## 142. refactor(api_keys): use a KMS encrypted API key hashing key and remove key ID prefix from plaintext API keys (#639)

- **Commit:** `3a3b33ac`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-03-05T21:08:48+05:30
- **Changes:** 17 files (+262/-105)

## 143. docs: Update naming conventions and added examples (#709)

- **Commit:** `98415193`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-03-06T16:53:32+05:30
- **Changes:** 22 files (+871/-620)

## 144. feat(connector): [Fiserv] add Refunds, Cancel and Wallets flow along with Unit Tests (#593)

- **Commit:** `cd1c5409`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-03-09T17:00:10+05:30
- **Changes:** 8 files (+1178/-333)

## 145. feat(connector): [Trustpay] add authorize (cards 3ds, no3ds and bank redirects), refund, psync, rsync (#717)

- **Commit:** `e102cae7`
- **Author:** saiharsha-juspay <99009240+saiharsha-juspay@users.noreply.github.com>
- **Date:** 2023-03-13T17:23:39+05:30
- **Changes:** 18 files (+2002/-11)

## 146. refactor: Basilisk hs integration (#704)

- **Commit:** `585618e5`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-03-14T13:22:07+05:30
- **Changes:** 15 files (+1068/-214)

## 147. feat(connector): add webhook support for worldline connector (#721)

- **Commit:** `13a8ce8e`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-03-14T14:36:27+05:30
- **Changes:** 5 files (+208/-74)

## 148. feat: add generic in-memory cache interface (#737)

- **Commit:** `7f5e5d86`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-03-14T17:48:46+05:30
- **Changes:** 4 files (+309/-40)

## 149. feat(connector): Add support for complete authorize payment after 3DS redirection (#741)

- **Commit:** `ec2b1b18`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-03-15T14:18:17+05:30
- **Changes:** 71 files (+1867/-628)

## 150. feat: Time based deletion of temp card (#729)

- **Commit:** `db3d3164`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-03-15T17:24:35+05:30
- **Changes:** 11 files (+262/-11)

## 151. refactor(kms): share a KMS client for all KMS operations (#744)

- **Commit:** `a3ff2e8d`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-03-15T21:53:38+05:30
- **Changes:** 14 files (+349/-308)

## 152. refactor(metrics): use macros for constructing counter and histogram metrics (#755)

- **Commit:** `58106d91`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-03-16T02:27:38+05:30
- **Changes:** 5 files (+104/-100)

## 153. feat(connector): add authorize, void, refund, psync, rsync support for mollie connector (#740)

- **Commit:** `168fa32f`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-03-16T12:43:01+05:30
- **Changes:** 19 files (+1032/-13)

## 154. refactor(connector): update add_connector script (#762)

- **Commit:** `78794ed6`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-03-17T11:19:23+05:30
- **Changes:** 5 files (+204/-89)

## 155. feat(connector): [Trustpay] add webhooks (payment and refund events) (#746)

- **Commit:** `853dfa16`
- **Author:** saiharsha-juspay <99009240+saiharsha-juspay@users.noreply.github.com>
- **Date:** 2023-03-20T11:32:23+05:30
- **Changes:** 30 files (+398/-86)

## 156. refactor: get connection pool based on olap/oltp features (#743)

- **Commit:** `a392fb16`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-03-20T11:35:10+05:30
- **Changes:** 18 files (+147/-146)

## 157. feat(router): adding metrics for tracking behavior throughout the `router` crate  (#768)

- **Commit:** `d302b286`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-03-21T11:03:03+05:30
- **Changes:** 28 files (+487/-77)

## 158. feat(core): accept gateway credentials in the request body in payments and refunds (#766)

- **Commit:** `cb188f92`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2023-03-21T14:37:41+05:30
- **Changes:** 35 files (+748/-130)

## 159. feat(router): add support for stateful straight through routing (#752)

- **Commit:** `568bf01a`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-03-21T17:26:37+05:30
- **Changes:** 27 files (+374/-236)

## 160. feat: add in-memory cache support for config table (#751)

- **Commit:** `abedaae4`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-03-21T17:26:48+05:30
- **Changes:** 8 files (+156/-70)

## 161. refactor: extract kms module to `external_services` crate (#793)

- **Commit:** `029e3894`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-03-24T14:31:59+05:30
- **Changes:** 15 files (+162/-67)

## 162. feat(connector): [Nuvei] add webhook support (#795)

- **Commit:** `20b4372b`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-03-28T18:56:32+05:30
- **Changes:** 7 files (+284/-84)

## 163. feat: cards info api (#749)

- **Commit:** `b15b8f7b`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-03-28T19:04:58+05:30
- **Changes:** 27 files (+1282/-245)

## 164. feat(connector): [Shift4] add eps, sofort, giropay, ideal support for shift4 connector (#810)

- **Commit:** `fb66a0e0`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-03-30T04:25:11+05:30
- **Changes:** 1 files (+215/-54)

## 165. feat(router): added incoming dispute webhooks flow (#769)

- **Commit:** `a733eafb`
- **Author:** saiharsha-juspay <99009240+saiharsha-juspay@users.noreply.github.com>
- **Date:** 2023-03-30T04:25:54+05:30
- **Changes:** 28 files (+1138/-31)

## 166. enhance(core): replace string with enum for country (#735)

- **Commit:** `e18bfb2a`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-03-30T21:45:38+05:30
- **Changes:** 45 files (+734/-649)

## 167. feat(connector) : h1075:L4 Hackathon globalpay wallet  (#625)

- **Commit:** `4d1013c6`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-03-30T22:51:22+05:30
- **Changes:** 34 files (+578/-176)

## 168. feat(core): added multiple payment_attempt support for payment_intent (#439)

- **Commit:** `35d3e277`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2023-03-30T23:49:51+05:30
- **Changes:** 29 files (+370/-505)

## 169. feat(request): add `RequestBuilder` method to attach default request headers (#826)

- **Commit:** `6f61f830`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-04-04T11:26:24+05:30
- **Changes:** 29 files (+272/-225)

## 170. feat(connector): add authorize, capture, void, psync, refund, rsync for PayPal connector (#747)

- **Commit:** `36049c13`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-04-06T19:06:43+05:30
- **Changes:** 19 files (+2190/-38)

## 171. feat: allow (de)serializing countries to/from alpha-2, alpha-3 and numeric country codes (#836)

- **Commit:** `899767cf`
- **Author:** Nachiket Kanore <44920607+nachiketkanore@users.noreply.github.com>
- **Date:** 2023-04-06T19:09:48+05:30
- **Changes:** 4 files (+2596/-4)

## 172. feat(connector): [Coinbase] [Opennode] Add support for crypto payments via PG redirection (#834)

- **Commit:** `b3d14737`
- **Author:** Arvind Patel <52006565+arvindpatel24@users.noreply.github.com>
- **Date:** 2023-04-11T13:05:57+05:30
- **Changes:** 43 files (+3054/-93)

## 173. feat(connector): [Worldpay] add support for webhook (#820)

- **Commit:** `23511166`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-04-11T13:07:28+05:30
- **Changes:** 7 files (+162/-50)

## 174. feat: connector tokenization flow (#750)

- **Commit:** `29da1dfa`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-04-11T17:24:45+05:30
- **Changes:** 70 files (+1441/-230)

## 175. feat: multiple connector account support for the same `country` (#816)

- **Commit:** `6188d515`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-04-11T17:25:29+05:30
- **Changes:** 40 files (+631/-52)

## 176. feat(connector) : [Globalpay]add  mandates and bank redirects support for globalpay (#830)

- **Commit:** `ce912dd8`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-04-11T17:46:01+05:30
- **Changes:** 6 files (+206/-78)

## 177. refactor(router_env): improve logging setup (#847)

- **Commit:** `1b94d25f`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-04-11T19:44:48+05:30
- **Changes:** 12 files (+271/-200)

## 178. feat(router): separate straight through algorithm in separate column in payment attempt (#863)

- **Commit:** `01f86c49`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-04-12T18:27:17+05:30
- **Changes:** 15 files (+104/-121)

## 179. build(deps): bump `fred` from `5.2.0` to `6.0.0` (#869)

- **Commit:** `01bc162d`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-04-13T13:28:51+05:30
- **Changes:** 5 files (+82/-150)

## 180. feat(connector): [Airwallex] add multiple redirect support for 3DS (#811)

- **Commit:** `d1d58e33`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-04-13T13:40:30+05:30
- **Changes:** 19 files (+374/-84)

## 181. feat(router): added dispute retrieve and dispute list apis (#842)

- **Commit:** `acab7671`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-04-13T14:04:49+05:30
- **Changes:** 24 files (+404/-31)

## 182. feat(connector) : add authorize,capture,void,refunds and mandates for payeezy (#800)

- **Commit:** `56952f28`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-04-13T16:06:27+05:30
- **Changes:** 22 files (+1585/-14)

## 183. feat(core): add backwards compatibility for multiple mca (#866)

- **Commit:** `cf902f19`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-04-13T17:04:36+05:30
- **Changes:** 11 files (+281/-145)

## 184. feat(connector) : add template code for connector forte (#854)

- **Commit:** `7a581a66`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-04-18T00:00:16+05:30
- **Changes:** 18 files (+1202/-13)

## 185. feat(connector): [Nuvei] add support for card mandates (#818)

- **Commit:** `298a0a49`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-04-18T00:00:54+05:30
- **Changes:** 10 files (+462/-242)

## 186. refactor(storage_models, errors): impl StorageErrorExt for error_stack::Result<T, errors::StorageError> (#886)

- **Commit:** `b4020294`
- **Author:** Abhishek <abhishek.marrivagu@juspay.in>
- **Date:** 2023-04-18T00:01:13+05:30
- **Changes:** 23 files (+125/-268)

## 187. feat(connector): [Shift4] add support for card 3DS payment (#828)

- **Commit:** `29999fe5`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-04-18T01:01:15+05:30
- **Changes:** 17 files (+570/-130)

## 188. feat(connector) : add template code for connector nexinets (#852)

- **Commit:** `dee5f615`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-04-18T13:15:17+05:30
- **Changes:** 16 files (+1191/-4)

## 189. chore(dependencies): Update dependencies for router packages (#902)

- **Commit:** `171c4120`
- **Author:** Sampras Lopes <lsampras@protonmail.com>
- **Date:** 2023-04-18T22:46:51+05:30
- **Changes:** 15 files (+472/-408)

## 190. feat(router): add new payment methods for Bank redirects, BNPL and wallet (#864)

- **Commit:** `304081cb`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-04-21T02:50:29+05:30
- **Changes:** 11 files (+948/-417)

## 191. feat(connector): [Checkout] add GooglePay, ApplePay and Webhooks support  (#875)

- **Commit:** `3fce1407`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-04-21T02:50:49+05:30
- **Changes:** 8 files (+969/-501)

## 192. feat: support gpay and applepay session response for all connectors (#839)

- **Commit:** `d23e14c5`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-04-21T02:52:40+05:30
- **Changes:** 11 files (+296/-651)

## 193. feat(connector) : add PayPal wallet support for Paypal (#893)

- **Commit:** `a475a76d`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-04-21T02:54:29+05:30
- **Changes:** 4 files (+288/-63)

## 194. feat(connector): [Nuvei] add support for bank redirect Eps, Sofort, Giropay, Ideal (#870)

- **Commit:** `c1a25b30`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-04-21T12:51:06+05:30
- **Changes:** 12 files (+1162/-152)

## 195. feat(core): [Stripe] add bank debits payment method to stripe (#906)

- **Commit:** `f624eb52`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-04-21T13:49:20+05:30
- **Changes:** 8 files (+345/-43)

## 196. feat(Core): gracefully shutdown router/scheduler if Redis is unavailable (#891)

- **Commit:** `13185999`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-04-24T13:08:00+05:30
- **Changes:** 21 files (+166/-74)

## 197. feat(router): added dispute accept api, file module apis and dispute evidence submission api  (#900)

- **Commit:** `bdf1e514`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-04-25T01:05:21+05:30
- **Changes:** 54 files (+2822/-34)

## 198. feat(connector): add 3ds for Bambora and Support Html 3ds response (#817)

- **Commit:** `20bea23b`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-04-25T01:06:12+05:30
- **Changes:** 11 files (+325/-87)

## 199. feat(connector): [Zen] add Cards 3DS, Non-3DS, GooglePay, ApplePay and Webhooks support  (#962)

- **Commit:** `71c39bda`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-04-25T20:14:29+05:30
- **Changes:** 16 files (+1590/-11)

## 200. refactor(stripe): return all the missing fields in a request (#935)

- **Commit:** `e9fc34ff`
- **Author:** Jeeva <jeevaprakashdr@hotmail.com>
- **Date:** 2023-05-02T21:26:52+01:00
- **Changes:** 9 files (+315/-28)

## 201. feat(connector): [ACI] Add banking redirect support for EPS, Giropay, iDEAL, and Sofortueberweisung (#890)

- **Commit:** `c86f2c04`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-05-03T01:57:32+05:30
- **Changes:** 6 files (+194/-19)

## 202. feat(cards): validate card security code and expiration (#874)

- **Commit:** `0b7bc7bc`
- **Author:** Naman Agarwal <naman.agarwal2019@vitstudent.ac.in>
- **Date:** 2023-05-03T02:13:38+05:30
- **Changes:** 5 files (+331/-5)

## 203. feat(router): added support for optional defend dispute api call and added evidence submission flow for checkout connector (#979)

- **Commit:** `4728d946`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-05-03T02:25:53+05:30
- **Changes:** 13 files (+529/-46)

## 204. feat(connector): add dispute webhooks for Stripe (#918)

- **Commit:** `0df22447`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-05-03T02:34:02+05:30
- **Changes:** 14 files (+348/-102)

## 205. refactor: use `CountryAlpha2` instead of `CountryCode` for country codes (#904)

- **Commit:** `2cff019a`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-05-03T13:46:41+05:30
- **Changes:** 39 files (+1952/-2427)

## 206. feat(connector) : add Cards(3ds & non3ds),bank_redirects ,wallets(Paypal,Applepay) and Mandates support to nexinets (#898)

- **Commit:** `eea05f5c`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-05-03T13:47:42+05:30
- **Changes:** 11 files (+1147/-251)

## 207. feat: PG Agnostic mandate using network_txns_id (Adyen, Authorizedotnet, Stripe) (#855)

- **Commit:** `ed99655e`
- **Author:** Manoj Ghorela <118727120+manoj-juspay@users.noreply.github.com>
- **Date:** 2023-05-03T15:48:51+05:30
- **Changes:** 72 files (+1128/-100)

## 208. feat: expire client secret after a merchant configurable intent fufliment time (#956)

- **Commit:** `03a96432`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-05-03T16:08:13+05:30
- **Changes:** 21 files (+201/-49)

## 209. feat(connector): add authorize, capture, void, psync, refund, rsync for Forte connector (#955)

- **Commit:** `f0464bc4`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-05-04T19:22:28+05:30
- **Changes:** 23 files (+997/-237)

## 210. refactor: use newtype pattern for email addresses (#819)

- **Commit:** `b8e2b1c5`
- **Author:** Nachiket Kanore <44920607+nachiketkanore@users.noreply.github.com>
- **Date:** 2023-05-04T19:28:20+05:30
- **Changes:** 30 files (+211/-145)

## 211. feat(connector): add dummy connector template code (#970)

- **Commit:** `e5cc0d9d`
- **Author:** ThisIsMani <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-05-04T19:29:59+05:30
- **Changes:** 18 files (+1246/-2)

## 212. feat(compatibility): add mandates support in stripe compatibility (#897)

- **Commit:** `2ba186b7`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-05-08T14:41:27+05:30
- **Changes:** 13 files (+329/-76)

## 213. feat(connector): add payment routes for dummy connector (#980)

- **Commit:** `4ece376b`
- **Author:** ThisIsMani <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-05-08T15:04:50+05:30
- **Changes:** 11 files (+320/-1)

## 214. feat(connector): [Bluesnap] add cards 3DS support  (#1057)

- **Commit:** `9c331e41`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-05-08T19:04:43+05:30
- **Changes:** 15 files (+596/-69)

## 215. feat(connector): Mandates for alternate payment methods via Stripe (#1041)

- **Commit:** `64721b80`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-05-08T19:08:15+05:30
- **Changes:** 32 files (+1068/-601)

## 216. feat(connector): Mandates for alternate payment methods via Adyen (#1046)

- **Commit:** `4403634d`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-05-09T19:49:55+05:30
- **Changes:** 23 files (+410/-30)

## 217. feat(cards): add credit card number validation (#889)

- **Commit:** `d6e71b95`
- **Author:** phillyphil91 <57916112+phillyphil91@users.noreply.github.com>
- **Date:** 2023-05-09T16:30:50+02:00
- **Changes:** 79 files (+381/-684)

## 218. feat(router): added retrieval flow for connector file uploads and added support for stripe connector (#990)

- **Commit:** `38aa9eab`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-05-09T20:10:54+05:30
- **Changes:** 16 files (+388/-66)

## 219. feat(connector): add dispute and refund webhooks for Airwallex (#1021)

- **Commit:** `8c341141`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-05-09T22:59:37+05:30
- **Changes:** 2 files (+212/-12)

## 220. feat(connector) : add bank redirect support for worldline (#1060)

- **Commit:** `bc4ac529`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-05-10T00:08:43+05:30
- **Changes:** 3 files (+214/-42)

## 221. feat(connector): [Iatapay] Implement AccessTokenAuth, Authorize, PSync, Refund, RSync and testcases (#1034)

- **Commit:** `a2527b5b`
- **Author:** Arvind Patel <52006565+arvindpatel24@users.noreply.github.com>
- **Date:** 2023-05-11T14:07:05+05:30
- **Changes:** 30 files (+1299/-10)

## 222. feat(connector): [bitpay] Add new crypto connector bitpay & testcases for all crypto connectors (#919)

- **Commit:** `f70f10aa`
- **Author:** Arvind Patel <52006565+arvindpatel24@users.noreply.github.com>
- **Date:** 2023-05-11T16:36:47+05:30
- **Changes:** 20 files (+1172/-719)

## 223. feat(connector): add connector nmi with card, applepay and googlepay support (#771)

- **Commit:** `baf5fd91`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-05-11T16:47:00+05:30
- **Changes:** 20 files (+2022/-7)

## 224. refactor(session_token): add support for business filtering in payments session (#1128)

- **Commit:** `2b0ed125`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-05-11T20:34:45+05:30
- **Changes:** 13 files (+127/-104)

## 225. feat(router): add payment, refund routes for dummy connector (#1071)

- **Commit:** `822fc695`
- **Author:** ThisIsMani <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-05-12T00:33:36+05:30
- **Changes:** 10 files (+438/-82)

## 226. feat(router): add attach dispute evidence api (#1070)

- **Commit:** `a5756aae`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-05-13T14:59:11+05:30
- **Changes:** 13 files (+350/-16)

## 227. feat(connector): add multiple dummy connectors and enable them (#1147)

- **Commit:** `8a35f7c9`
- **Author:** ThisIsMani <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-05-13T15:35:20+05:30
- **Changes:** 6 files (+168/-57)

## 228. feat(connector): [Noon] Add script generated template code  (#1164)

- **Commit:** `bfaf75fc`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-05-16T16:20:39+05:30
- **Changes:** 16 files (+1194/-22)

## 229. feat(router): add retrieve dispute evidence API (#1114)

- **Commit:** `354ee013`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-05-16T17:34:47+05:30
- **Changes:** 8 files (+264/-0)

## 230. feat(router): implement `ApiKeyInterface` for `MockDb` (#1101)

- **Commit:** `95c7ca99`
- **Author:** Derek Leverenz <derek@derekleverenz.com>
- **Date:** 2023-05-16T11:35:50-07:00
- **Changes:** 3 files (+225/-26)

## 231. feat(email): integrate email service using AWS SES (#1158)

- **Commit:** `07e0fcbe`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-05-17T15:12:32+05:30
- **Changes:** 9 files (+226/-33)

## 232. feat(connector): [Bluesnap] Add support for ApplePay (#1178)

- **Commit:** `919c03e6`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-05-17T18:40:20+05:30
- **Changes:** 5 files (+323/-17)

## 233. feat(payments): add support for manual retries in payments confirm call (#1170)

- **Commit:** `1f52a664`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-05-18T13:46:38+05:30
- **Changes:** 5 files (+270/-25)

## 234. feat(connector): [Authorizedotnet] implement Capture flow and webhooks for Authorizedotnet (#1171)

- **Commit:** `2d49ce56`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-05-18T20:11:52+05:30
- **Changes:** 3 files (+1067/-455)

## 235. refactor(mandate): allow merchant to pass the mandate details and customer acceptance separately (#1188)

- **Commit:** `6c41cdb1`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-05-19T12:19:19+05:30
- **Changes:** 20 files (+220/-47)

## 236. feat: ACH transfers (#905)

- **Commit:** `23bca66b`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-05-19T15:14:29+05:30
- **Changes:** 39 files (+1247/-66)

## 237. feat(documentation): add polymorphic `generate_schema` macro (#1183)

- **Commit:** `53aa5ac9`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-05-19T16:37:54+05:30
- **Changes:** 14 files (+4703/-3353)

## 238. feat: SEPA and BACS bank transfers through stripe (#930)

- **Commit:** `cf000599`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-05-19T18:05:10+05:30
- **Changes:** 9 files (+423/-82)

## 239. feat(connector): [Noon] Add Card Payments, Capture, Void and Refund (#1207)

- **Commit:** `27610361`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-05-23T16:35:39+05:30
- **Changes:** 8 files (+430/-116)

## 240. feat(kms): reduce redundant kms calls (#1264)

- **Commit:** `71a17c68`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-05-25T14:35:40+05:30
- **Changes:** 8 files (+143/-153)

## 241. build(deps): bump `diesel` from `2.0.3` to `2.1.0` (#1287)

- **Commit:** `b9ec38a1`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-05-29T13:57:27+05:30
- **Changes:** 14 files (+477/-263)

## 242. fix(router/webhooks): use api error response for returning errors from webhooks core (#1305)

- **Commit:** `cd0cf40f`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-05-29T19:28:38+05:30
- **Changes:** 6 files (+212/-109)

## 243. feat: encrypt PII fields before saving it in the database (#1043)

- **Commit:** `fa392c40`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-05-30T13:43:17+05:30
- **Changes:** 107 files (+3817/-1266)

## 244. fix(router/webhooks): correct webhook error mapping and make source verification optional for all connectors (#1333)

- **Commit:** `71315097`
- **Author:** ItsMeShashank <shashank.attarde@juspay.in>
- **Date:** 2023-06-02T15:30:37+05:30
- **Changes:** 23 files (+191/-114)

## 245. test(selenium): read config from `CONNECTOR_AUTH_FILE_PATH` environment variable and fix bugs in UI tests (#1225)

- **Commit:** `d9a16ed5`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-06-05T13:00:00+05:30
- **Changes:** 13 files (+738/-118)

## 246. feat(db): implement `DisputeInterface` for `MockDb` (#1345)

- **Commit:** `e5e39a74`
- **Author:** Raphaël Castaigne <rcastaigne@gmail.com>
- **Date:** 2023-06-05T09:30:44+02:00
- **Changes:** 3 files (+679/-26)

## 247. feat(headers): add optional header masking feature to outbound request (#1320)

- **Commit:** `fc6acd04`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-06-05T13:10:14+05:30
- **Changes:** 43 files (+938/-527)

## 248. feat(connector): [Noon] Add Card Mandates and Webhooks Support (#1243)

- **Commit:** `ba8a17d6`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-06-05T15:06:59+05:30
- **Changes:** 16 files (+256/-34)

## 249. refactor(router): remove `pii-encryption-script` feature and use of timestamps for decryption (#1350)

- **Commit:** `9f2832f6`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-06-05T18:18:00+05:30
- **Changes:** 24 files (+52/-585)

## 250. refactor(webhook): added the unknown field to the webhook_event_status of every connector (#1343)

- **Commit:** `65d4a95b`
- **Author:** Aprabhat19 <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2023-06-05T20:00:29+05:30
- **Changes:** 48 files (+199/-45)

## 251. feat(ci): Create a new workflow to validate the generated openAPI spec file (openapi_spec.json) (#1323)

- **Commit:** `6730fe32`
- **Author:** Kritik Modi <61862301+kritikmodi@users.noreply.github.com>
- **Date:** 2023-06-06T19:14:42+05:30
- **Changes:** 9 files (+2055/-616)

## 252. fix(config): fix docker compose local setup (#1372)

- **Commit:** `d21fcc7b`
- **Author:** Sampras Lopes <lsampras@protonmail.com>
- **Date:** 2023-06-07T15:15:52+05:30
- **Changes:** 29 files (+84/-511)

## 253. feat: Session flow for Apple Pay trustpay (#1155)

- **Commit:** `a6e91a82`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-06-07T20:27:19+05:30
- **Changes:** 23 files (+541/-115)

## 254. build(deps): update dependencies (#1342)

- **Commit:** `bce01ced`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-06-07T23:27:04+05:30
- **Changes:** 26 files (+509/-1118)

## 255. feat(connector): [Zen] add apple pay redirect flow support for zen connector (#1383)

- **Commit:** `b3b16fcf`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-06-08T02:25:28+05:30
- **Changes:** 3 files (+406/-117)

## 256. docs: add `ApplePayRedirectionData` to OpenAPI schema (#1386)

- **Commit:** `d0d32544`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-06-08T15:01:32+05:30
- **Changes:** 2 files (+325/-223)

## 257. fix: revert session flow for Apple Pay trustpay (#1393)

- **Commit:** `0ca69e60`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-06-08T22:15:21+05:30
- **Changes:** 23 files (+115/-541)

## 258. feat(payment): customer ip field inclusion (#1370)

- **Commit:** `11a827a7`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-06-09T12:30:39+05:30
- **Changes:** 12 files (+460/-122)

## 259. ci: update versions of actions (#1388)

- **Commit:** `638fc422`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-06-09T13:18:42+05:30
- **Changes:** 11 files (+284/-358)

## 260. fix(connector): [Bluesnap] Throw proper error message for redirection scenario (#1367)

- **Commit:** `4a8de774`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-06-09T19:38:28+05:30
- **Changes:** 11 files (+192/-92)

## 261. feat(connector): mask pii information in connector request and response for stripe, bluesnap, checkout, zen (#1435)

- **Commit:** `5535159d`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-06-14T17:43:27+05:30
- **Changes:** 6 files (+111/-111)

## 262. feat(order_details): Adding order_details both inside and outside of metadata, in payments request, for backward compatibility (#1344)

- **Commit:** `913b8331`
- **Author:** rishavkar <73836104+rishavkar@users.noreply.github.com>
- **Date:** 2023-06-14T22:12:33+05:30
- **Changes:** 19 files (+581/-209)

## 263. test(connector): [Globalpay] Fix unit tests (#1217)

- **Commit:** `71c0d4c5`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-06-15T12:49:07+05:30
- **Changes:** 5 files (+310/-61)

## 264. fix(connector): implement ConnectorErrorExt for error_stack::Result<T, ConnectorError> (#1382)

- **Commit:** `3ef1d293`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-06-16T18:51:29+05:30
- **Changes:** 12 files (+142/-132)

## 265. refactor(core): accept customer data in customer object (#1447)

- **Commit:** `cff1ce61`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-06-16T18:55:01+05:30
- **Changes:** 11 files (+195/-66)

## 266. refactor(fix): [Adyen] Fix bug in Adyen (#1375)

- **Commit:** `d3a69060`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-06-16T20:14:24+05:30
- **Changes:** 8 files (+134/-303)

## 267. chore(common_utils): Apply the new type pattern for phone numbers (#1286)

- **Commit:** `98e73e2e`
- **Author:** vlad-onis <107788332+vlad-onis@users.noreply.github.com>
- **Date:** 2023-06-16T20:45:10+03:00
- **Changes:** 5 files (+307/-89)

## 268. feat: applepay through trustpay (#1422)

- **Commit:** `8032e029`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-06-18T20:36:57+05:30
- **Changes:** 21 files (+694/-147)

## 269. refactor(core): move update trackers after build request (#1472)

- **Commit:** `6114fb63`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-06-19T13:04:45+05:30
- **Changes:** 32 files (+327/-209)

## 270. feat(router): add route to invalidate cache entry (#1100)

- **Commit:** `21f2ccd4`
- **Author:** Jeeva <jeevaprakashdr@hotmail.com>
- **Date:** 2023-06-21T08:40:03+01:00
- **Changes:** 14 files (+271/-43)

## 271. feat: fetch merchant key store only once per session (#1400)

- **Commit:** `d321aa1f`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-06-22T14:40:28+05:30
- **Changes:** 65 files (+979/-498)

## 272. feat(connector): enforce logging for connector requests (#1467)

- **Commit:** `e575fde6`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-06-22T15:08:32+05:30
- **Changes:** 51 files (+1082/-751)

## 273. fix(connector): Convert state of US and CA in ISO format for cybersource connector (#1506)

- **Commit:** `4a047ce1`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-06-22T18:40:02+05:30
- **Changes:** 5 files (+212/-4)

## 274. feat(connector): Add connector cashtocode (#1429)

- **Commit:** `784847b0`
- **Author:** BallaNitesh <126162378+BallaNitesh@users.noreply.github.com>
- **Date:** 2023-06-27T15:05:23+05:30
- **Changes:** 25 files (+888/-26)

## 275. feat(connector): [Adyen] Add support for Samsung Pay (#1525)

- **Commit:** `33309daf`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-06-28T14:34:49+05:30
- **Changes:** 6 files (+577/-342)

## 276. feat(connector): [Payme] Add template code for Payme connector (#1486)

- **Commit:** `5305a7b2`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-06-28T16:57:20+05:30
- **Changes:** 18 files (+1170/-27)

## 277. test(connector): Add tests for Globalpay and Bluesnap (#1281)

- **Commit:** `c5ff6ed4`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-06-28T23:10:14+05:30
- **Changes:** 4 files (+271/-0)

## 278. feat(connector): [Opayo] Add script generated template code (#1295)

- **Commit:** `60e15dda`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-06-30T10:28:30+05:30
- **Changes:** 17 files (+1178/-9)

## 279. feat(connector): [ACI] implement Card Mandates for ACI (#1174)

- **Commit:** `15c2a70b`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-06-30T13:11:17+05:30
- **Changes:** 3 files (+406/-175)

## 280. feat(connector): [cryptopay] add new connector cryptopay, authorize, sync, webhook and testcases (#1511)

- **Commit:** `7bb0aa5c`
- **Author:** Arvind Patel <52006565+arvindpatel24@users.noreply.github.com>
- **Date:** 2023-06-30T14:57:35+05:30
- **Changes:** 24 files (+872/-15)

## 281. feat(router): add filters for refunds (#1501)

- **Commit:** `88860b9c`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-06-30T18:24:41+05:30
- **Changes:** 10 files (+342/-60)

## 282. feat(payment_method): [upi] add new payment method and use in iatapay (#1528)

- **Commit:** `2d11bf5b`
- **Author:** Arvind Patel <52006565+arvindpatel24@users.noreply.github.com>
- **Date:** 2023-06-30T19:54:35+05:30
- **Changes:** 10 files (+282/-183)

## 283. feat: add `merchant_name` field in the response body (#1280)

- **Commit:** `dd4ba63c`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2023-07-01T16:40:46+05:30
- **Changes:** 3 files (+242/-267)

## 284. feat(connector): [TrustPay] Add Google Pay support (#1515)

- **Commit:** `47cd08a0`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-07-01T17:15:06+05:30
- **Changes:** 10 files (+647/-308)

## 285. ci(validate-openapi-spec): fail check if OpenAPI spec is not up-to-date (#1582)

- **Commit:** `7b21777b`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-07-04T11:29:59+05:30
- **Changes:** 6 files (+249/-206)

## 286. feat(email): implement process_tracker for scheduling email when api_key is about to expire (#1233)

- **Commit:** `ee7cdef1`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-07-04T12:01:22+05:30
- **Changes:** 10 files (+457/-17)

## 287. feat: list payment_methods with the required fields in each method (#1310)

- **Commit:** `6447b045`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-07-04T19:11:55+05:30
- **Changes:** 8 files (+1004/-3)

## 288. feat(payments): add connector_metadata, metadata and feature_metadata fields in payments, remove udf field (#1595)

- **Commit:** `e713b62a`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-07-05T17:51:05+05:30
- **Changes:** 20 files (+476/-438)

## 289. feat(router): add card_info in payment_attempt table if not provided in request (#1538)

- **Commit:** `5628985c`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-07-05T18:28:00+05:30
- **Changes:** 23 files (+230/-46)

## 290. feat(test): Add support to run UI tests in CI pipeline (#1539)

- **Commit:** `21f5e209`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-07-05T19:01:42+05:30
- **Changes:** 12 files (+1407/-92)

## 291. feat(connector): [Stripe] implement Multibanco Bank Transfer for stripe  (#1420)

- **Commit:** `ca4e242d`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-07-06T13:22:48+05:30
- **Changes:** 12 files (+214/-37)

## 292. feat(connector): [Globepay] Add template code for Globepay connector (#1623)

- **Commit:** `06f92c2c`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-07-06T17:44:36+05:30
- **Changes:** 15 files (+1159/-5)

## 293. feat: add cache for api_key and mca tables (#1212)

- **Commit:** `fc9057ef`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-07-07T12:10:49+05:30
- **Changes:** 3 files (+373/-54)

## 294. feat(connector): [Payme] add Authorize, Sync, Capture, Refund, Refund Sync, Mandate & web hooks support for cards (#1594)

- **Commit:** `093cc6a7`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-07-07T12:40:02+05:30
- **Changes:** 9 files (+803/-264)

## 295. feat(router): get filters for payments (#1600)

- **Commit:** `d5891ecb`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-07-07T16:10:01+05:30
- **Changes:** 12 files (+341/-15)

## 296. feat(connector): [PowerTranz] Add template code for PowerTranz connector (#1650)

- **Commit:** `f56f9d64`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-07-07T19:51:07+05:30
- **Changes:** 16 files (+1173/-3)

## 297. ci(runner): rewrite `collection_runner.sh` in rust (#1604)

- **Commit:** `e09077a7`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-07-10T15:02:44+05:30
- **Changes:** 17 files (+496/-240)

## 298. feat(pm_list): add required field info for crypto pay (#1655)

- **Commit:** `6d4943d8`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-07-10T19:19:28+05:30
- **Changes:** 3 files (+277/-132)

## 299. fix(core): Fix wallet payments throwing `Invalid 'payment_method_type' provided` and UI test issues (#1633)

- **Commit:** `307a470f`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-07-10T22:48:07+05:30
- **Changes:** 18 files (+1412/-1315)

## 300. refactor: include binary name in `crates_to_filter` for logging (#1689)

- **Commit:** `123b34c7`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-07-12T17:00:32+05:30
- **Changes:** 11 files (+306/-43)

## 301. refactor(storage): update crate name to diesel models (#1685)

- **Commit:** `5a0e8be8`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-07-12T18:20:55+05:30
- **Changes:** 159 files (+338/-346)

## 302. fix(compatibility): fix mismatched fields in the payments flow  (#1640)

- **Commit:** `e0113b98`
- **Author:** Kritik Modi <61862301+kritikmodi@users.noreply.github.com>
- **Date:** 2023-07-12T23:05:14+05:30
- **Changes:** 2 files (+140/-87)

## 303. feat(connector): [Globepay] add authorize and psync flow  (#1639)

- **Commit:** `c119bfdd`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-07-13T14:06:25+05:30
- **Changes:** 10 files (+334/-284)

## 304. feat(connector): [PowerTranz] Add cards support for PowerTranz connector (#1687)

- **Commit:** `07120bf4`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-07-13T15:14:50+05:30
- **Changes:** 14 files (+522/-278)

## 305. refactor(enums): move enums from `storage_models` and `api_models` crates to `common_enums` crate (#1265)

- **Commit:** `c0e1d4d3`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2023-07-13T17:42:14+05:30
- **Changes:** 40 files (+991/-1852)

## 306. fix: store and retrieve merchant secret from MCA table for webhooks source verification (#1331)

- **Commit:** `a6645bd3`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-07-14T12:13:33+05:30
- **Changes:** 39 files (+271/-439)

## 307. feat(router): add expand attempts support in payments retrieve response (#1678)

- **Commit:** `8572f1da`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-07-14T12:14:57+05:30
- **Changes:** 24 files (+381/-0)

## 308. feat(connector): [Tsys] Add template code for Tsys connector (#1704)

- **Commit:** `76098952`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-07-14T12:56:44+05:30
- **Changes:** 16 files (+1154/-7)

## 309. refactor(payment_methods): Remove legacy locker code  as it is not been used (#1666)

- **Commit:** `8832dd60`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-07-14T15:21:10+05:30
- **Changes:** 9 files (+53/-269)

## 310. feat(connector): [Authorizedotnet] Add Wallet support (#1223)

- **Commit:** `05540ea1`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-07-14T15:23:48+05:30
- **Changes:** 6 files (+386/-74)

## 311. feat(connector): [Globepay] Add Refund and Refund Sync flow (#1706)

- **Commit:** `c72a592e`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-07-14T20:28:13+05:30
- **Changes:** 5 files (+225/-66)

## 312. feat(connector): [Mollie] Implement card 3ds (#1421)

- **Commit:** `91f969a2`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-07-16T18:12:33+05:30
- **Changes:** 18 files (+335/-288)

## 313. refactor(pm_list): Update required fields for a payment method (#1720)

- **Commit:** `8dd9fcc2`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-07-17T01:22:05+05:30
- **Changes:** 3 files (+384/-238)

## 314. feat(connector): [PowerTranz] Add cards 3ds support for PowerTranz connector (#1722)

- **Commit:** `95a45e49`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-07-17T09:36:11+05:30
- **Changes:** 5 files (+492/-45)

## 315. feat(connector): [Tsys] Add cards for Payments and Refunds flow (#1716)

- **Commit:** `714cd275`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-07-17T09:46:29+05:30
- **Changes:** 8 files (+617/-170)

## 316. revert: refactor(pm_list): Update required fields for a payment method (#1724)

- **Commit:** `c6f74554`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-07-17T13:08:56+05:30
- **Changes:** 3 files (+238/-384)

## 317. fix(router): Convert ephemeral to client secret auth list payment_method_customer (#1602)

- **Commit:** `5fbd1cc3`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-07-17T16:41:29+05:30
- **Changes:** 8 files (+274/-77)

## 318. feat(mandates): recurring payment support for bank redirect and bank debit payment method for stripe (#1119)

- **Commit:** `14c2d725`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-07-17T18:19:31+05:30
- **Changes:** 20 files (+385/-103)

## 319. feat(compatibility): add support for stripe compatible webhooks (#1728)

- **Commit:** `87ae99f7`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-07-17T18:40:24+05:30
- **Changes:** 8 files (+155/-68)

## 320. refactor(router): remove `WebhookApiErrorSwitch ` and implement error mapping using `ErrorSwitch` (#1660)

- **Commit:** `a7c66dde`
- **Author:** Panagiotis Ganelis <50522617+PanGan21@users.noreply.github.com>
- **Date:** 2023-07-17T20:57:01+03:00
- **Changes:** 5 files (+257/-277)

## 321. feat(connector): [Stax] Add template code for Stax connector (#1698)

- **Commit:** `f932d66c`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-07-18T13:28:17+05:30
- **Changes:** 17 files (+1163/-4)

## 322. test(connector): [Aci] Add UI test for Aci Payment Methods (#1702)

- **Commit:** `fe7a5b03`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-07-18T18:34:43+05:30
- **Changes:** 4 files (+299/-1)

## 323. test(connector): [Adyen] Add UI test for Adyen Payment methods (#1648)

- **Commit:** `2e9b7832`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-07-19T13:16:43+05:30
- **Changes:** 6 files (+450/-31)

## 324. fix(connector): stripe mandate failure and other ui tests failures (#1742)

- **Commit:** `ea119eb8`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-07-19T19:52:34+05:30
- **Changes:** 7 files (+137/-65)

## 325. feat: add payout service (#1665)

- **Commit:** `763e2df3`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2023-07-19T23:32:05+05:30
- **Changes:** 86 files (+9337/-232)

## 326. fix: remove payout test cases from connector-template (#1757)

- **Commit:** `d433a98d`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2023-07-20T12:40:44+05:30
- **Changes:** 1 files (+0/-209)

## 327. fix(router): Add additional card info in payment response (#1745)

- **Commit:** `a891708f`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-07-21T02:23:00+05:30
- **Changes:** 4 files (+143/-74)

## 328. fix(core): Address 500 when deleting payment method and add logs to postman collections (#1695)

- **Commit:** `df3970f2`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-07-24T17:29:10+05:30
- **Changes:** 9 files (+64/-7237)

## 329. revert: connector_label in webhook url is reverted back to connector_name (#1779)

- **Commit:** `a229c37a`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-07-25T09:58:28+05:30
- **Changes:** 7 files (+168/-46)

## 330. fix(connector): [Paypal] fix amount to its currency base unit (#1780)

- **Commit:** `f40d1441`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-07-25T11:28:43+05:30
- **Changes:** 4 files (+266/-12)

## 331. feat(connector): [Boku] Template generation (#1760)

- **Commit:** `78c6ccea`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-07-25T12:33:21+05:30
- **Changes:** 17 files (+1162/-3)

## 332. feat(macro): add config validation macro for connectors (#1755)

- **Commit:** `37a06516`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-07-25T12:42:18+05:30
- **Changes:** 7 files (+117/-87)

## 333. feat(connector): [Adyen] Add pix support for adyen (#1703)

- **Commit:** `33a1368e`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-07-25T19:40:45+05:30
- **Changes:** 10 files (+280/-181)

## 334. refactor(core): use secrets for connector AuthType in connector integration (#1441)

- **Commit:** `d068569f`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-07-26T17:04:49+05:30
- **Changes:** 80 files (+491/-393)

## 335. feat(core): Changed frm_config format type in merchant_connector_account and added frm_message in payments response (#1543)

- **Commit:** `c284f41c`
- **Author:** rishavkar <73836104+rishavkar@users.noreply.github.com>
- **Date:** 2023-07-26T18:15:26+05:30
- **Changes:** 38 files (+664/-108)

## 336. feat(router): apply filters on payments (#1744)

- **Commit:** `04c3de73`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-07-26T18:53:36+05:30
- **Changes:** 9 files (+254/-63)

## 337. revert: feat(connector): [Adyen] Add pix support for adyen (#1795)

- **Commit:** `38f14b9f`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-07-26T20:46:15+05:30
- **Changes:** 10 files (+181/-280)

## 338. feat(connector): [Zen] Add Latam Payment Methods (#1670)

- **Commit:** `4df67adb`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-07-27T00:54:45+05:30
- **Changes:** 21 files (+494/-30)

## 339. fix(router): add validation for all the connector auth type (#1748)

- **Commit:** `1cda7ad5`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2023-07-27T11:54:16+05:30
- **Changes:** 52 files (+411/-23)

## 340. feat(dummy_connector): Add 3DS Flow, Wallets and Pay Later for Dummy Connector (#1781)

- **Commit:** `8186c778`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-07-27T19:30:03+05:30
- **Changes:** 14 files (+1091/-283)

## 341. fix(connector):  Refactor capture and refund flow for Connectors (#1821)

- **Commit:** `d06adc70`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-08-01T12:19:56+05:30
- **Changes:** 4 files (+39/-437)

## 342. refactor(multiple_mca): make `primary_business_detail` optional and remove default values (#1677)

- **Commit:** `9c7ac624`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-08-01T12:45:44+05:30
- **Changes:** 8 files (+85/-127)

## 343. feat(connector): [Stax] Implement Cards for Connector Stax (#1773)

- **Commit:** `f492d0a9`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-08-01T13:37:28+05:30
- **Changes:** 9 files (+941/-218)

## 344. refactor(ui_tests): move ui_tests to test_utils crate to reduce development time (#1822)

- **Commit:** `5773faf7`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-08-01T16:22:51+05:30
- **Changes:** 74 files (+422/-122)

## 345. feat(connector): [Adyen] Implement Boleto Bancario in Vouchers and Add support for Voucher in Next Action (#1657)

- **Commit:** `801946f2`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-08-01T18:27:56+05:30
- **Changes:** 9 files (+246/-3)

## 346. feat(payment_methods): Added value Field in required Field for Pre-filling (#1827)

- **Commit:** `e047a11d`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2023-08-01T18:28:26+05:30
- **Changes:** 6 files (+521/-703)

## 347. fix(connector): refactor psync and rsync for connectors (#1830)

- **Commit:** `7a0d6f69`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-08-01T20:11:43+05:30
- **Changes:** 9 files (+69/-363)

## 348. fix(payments): write a foreign_from implementation for payment_method_data and add missing payment methods in helpers.rs (#1801)

- **Commit:** `50298c19`
- **Author:** Kritik Modi <61862301+kritikmodi@users.noreply.github.com>
- **Date:** 2023-08-01T23:51:21+05:30
- **Changes:** 4 files (+167/-48)

## 349. refactor(config): Add new type for kms encrypted values (#1823)

- **Commit:** `73ed7ae7`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-08-02T14:25:23+05:30
- **Changes:** 21 files (+214/-177)

## 350. feat(connector): [Boku] Implement Authorize, Psync, Refund and Rsync flow (#1699)

- **Commit:** `9cba7da0`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-08-02T14:58:22+05:30
- **Changes:** 14 files (+568/-159)

## 351. feat(connector):  add support for bank redirect for Paypal (#1107)

- **Commit:** `57887bdf`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-08-02T17:17:34+05:30
- **Changes:** 10 files (+388/-16)

## 352. feat(connector): [Adyen] implement Adyen bank transfers and voucher payments in Indonesia   (#1804)

- **Commit:** `9977f9d4`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-08-02T19:04:33+05:30
- **Changes:** 13 files (+952/-163)

## 353. feat(connector): [Adyen] Add support for gift cards balance (#1672)

- **Commit:** `c4796ffd`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-08-03T16:36:26+05:30
- **Changes:** 16 files (+373/-44)

## 354. feat(connector): [Square] Add template code for connector Square (#1834)

- **Commit:** `80b74e09`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-08-03T17:51:44+05:30
- **Changes:** 16 files (+1181/-5)

## 355. refactor(connector): use utility function to raise payment method not implemented errors (#1847)

- **Commit:** `f2fcc259`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-08-03T18:16:37+05:30
- **Changes:** 8 files (+542/-82)

## 356. feat(connector): [Payme] Add Sync, RSync & webhook flow support (#1862)

- **Commit:** `80579805`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-08-04T19:00:23+05:30
- **Changes:** 2 files (+371/-71)

## 357. revert: fix(core): add validation for all the connector auth_type (#1833)

- **Commit:** `ae3d25e6`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2023-08-04T18:58:43+05:30
- **Changes:** 51 files (+287/-451)

## 358. fix(connector): [DummyConnector] add new icons and fix `we_chat_pay` (#1845)

- **Commit:** `985ff6ba`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-08-07T14:21:11+05:30
- **Changes:** 10 files (+251/-147)

## 359. test(connector):  Add support for webhook tests  (#1863)

- **Commit:** `7b2c419c`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-08-08T12:36:45+05:30
- **Changes:** 10 files (+253/-12)

## 360. feat(connector): [Checkout] unify error code, message and reason in error response (#1855)

- **Commit:** `e8a51c2a`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-08-08T13:04:24+05:30
- **Changes:** 2 files (+221/-39)

## 361. feat(connector): [Adyen] Implement Open Banking Uk in Bank Redirects (#1802)

- **Commit:** `b9f12708`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-08-08T17:12:36+05:30
- **Changes:** 14 files (+223/-16)

## 362. feat(connector): [Stax] Implement Bank Debits and Webhooks for Connector Stax (#1832)

- **Commit:** `0f2bb6c0`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-08-08T20:07:00+05:30
- **Changes:** 8 files (+207/-12)

## 363. feat(router): add support for multiple partial capture (#1721)

- **Commit:** `c333fb7f`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-08-09T01:56:27+05:30
- **Changes:** 38 files (+1082/-336)

## 364. feat(docs): add multiple examples support and webhook schema (#1864)

- **Commit:** `f8ef52c6`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-08-09T11:25:56+05:30
- **Changes:** 6 files (+317/-12)

## 365. fix(router): handle JSON connector response parse error (#1892)

- **Commit:** `393c2ab9`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-08-09T12:17:59+05:30
- **Changes:** 4 files (+123/-89)

## 366. feat(connector): [Adyen] implement Japanese convenience stores (#1819)

- **Commit:** `a6fdf6dc`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-08-09T21:21:45+05:30
- **Changes:** 14 files (+277/-8)

## 367. refactor(storage): Add a separate crate to represent store implementations (#1853)

- **Commit:** `32b731d9`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-08-10T12:55:02+05:30
- **Changes:** 14 files (+853/-423)

## 368. feat(router): add webhook source verification support for multiple mca of the same connector (#1897)

- **Commit:** `3554fec1`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-08-10T15:24:17+05:30
- **Changes:** 10 files (+230/-30)

## 369. feat(connector): [PayMe] Implement preprocessing flow for cards (#1904)

- **Commit:** `38b9c077`
- **Author:** Sangamesh Kulkarni <59434228+Sangamesh26@users.noreply.github.com>
- **Date:** 2023-08-10T23:30:55+05:30
- **Changes:** 17 files (+404/-186)

## 370. refactor(storage): add redis structs to storage impls (#1910)

- **Commit:** `3e269663`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-08-11T12:50:38+05:30
- **Changes:** 9 files (+306/-133)

## 371. refactor(storage_impl): Integrate the composite store from external crate (#1921)

- **Commit:** `9f199d9a`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-08-14T18:46:31+05:30
- **Changes:** 44 files (+493/-448)

## 372. feat(router): send 2xx payments response for all the connector http responses (2xx, 4xx etc.) (#1924)

- **Commit:** `0ab6827f`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-08-17T15:26:07+05:30
- **Changes:** 18 files (+314/-223)

## 373. feat(business_profile): add business profile table and CRUD endpoints (#1928)

- **Commit:** `53956d6f`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-08-18T14:53:29+05:30
- **Changes:** 23 files (+933/-9)

## 374. feat(router): add total count for refunds list (#1935)

- **Commit:** `84967d39`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-08-18T19:29:12+05:30
- **Changes:** 4 files (+262/-8)

## 375. feat(storage_impl): split payment intent interface implementation (#1946)

- **Commit:** `88d65a62`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-08-21T19:23:03+05:30
- **Changes:** 43 files (+2280/-690)

## 376. fix(core): Update Webhooks Event Mapping and Forced Psync preconditions (#1970)

- **Commit:** `8cf1f75f`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-08-22T01:18:05+05:30
- **Changes:** 6 files (+101/-99)

## 377. fix: storage of generic payment methods in permanent locker (#1799)

- **Commit:** `19ee324d`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2023-08-22T12:19:43+05:30
- **Changes:** 5 files (+140/-133)

## 378. feat(core): add psync for multiple partial captures (#1934)

- **Commit:** `5657ad69`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-08-23T10:13:54+05:30
- **Changes:** 30 files (+1216/-1017)

## 379. feat(pm_list): add  card pm required field info for connectors (#1918)

- **Commit:** `52e01769`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-08-23T14:48:42+05:30
- **Changes:** 3 files (+1781/-189)

## 380. refactor(core): made authenticate_client_secret function public (#1992)

- **Commit:** `69867726`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-08-23T16:00:16+05:30
- **Changes:** 2 files (+338/-60)

## 381. feat(connector): fail payment authorize when capture_method is manual_method (#1893)

- **Commit:** `bca9d501`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-08-23T18:42:47+05:30
- **Changes:** 49 files (+790/-120)

## 382. feat(business_profile): add profile id in affected tables and modify api contract (#1971)

- **Commit:** `fe8d4c2e`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-08-23T19:34:37+05:30
- **Changes:** 29 files (+346/-76)

## 383. test: move Postman collections to directory structure (#1995)

- **Commit:** `b7e4048e`
- **Author:** Natarajan K <knutties@gmail.com>
- **Date:** 2023-08-24T15:09:25+05:30
- **Changes:** 6637 files (+323562/-149793)

## 384. feat(api_client): add api client trait (#1919)

- **Commit:** `97b27474`
- **Author:** harsh-sharma-juspay <125131007+harsh-sharma-juspay@users.noreply.github.com>
- **Date:** 2023-08-24T15:46:09+05:30
- **Changes:** 3 files (+226/-8)

## 385. feat(connector): [Braintree] Add Authorize, Capture, Void, PSync, Refund, Rsync for Braintree GraphQL API (#1962)

- **Commit:** `820f6153`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-08-24T19:12:43+05:30
- **Changes:** 15 files (+1901/-268)

## 386. feat(connector): [CashToCode] perform currency based connector credentials mapping (#2025)

- **Commit:** `7c0c3b6b`
- **Author:** BallaNitesh <126162378+BallaNitesh@users.noreply.github.com>
- **Date:** 2023-08-28T09:29:57+05:30
- **Changes:** 23 files (+184/-130)

## 387. chore: address Rust 1.72 clippy lints (#2011)

- **Commit:** `eaefa6e1`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-08-29T00:33:57+05:30
- **Changes:** 29 files (+178/-106)

## 388. feat(connector): [Paypal] add support for payment and refund webhooks (#2003)

- **Commit:** `ade27f01`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-08-29T10:53:55+05:30
- **Changes:** 4 files (+228/-84)

## 389. feat(connector): [HELCIM] Add template code for Helcim (#2019)

- **Commit:** `d804b232`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-08-29T11:54:02+05:30
- **Changes:** 16 files (+1174/-2)

## 390. feat(connector): (globalpay) add support for multilple partial capture (#2035)

- **Commit:** `a93eea73`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-08-29T16:37:25+05:30
- **Changes:** 5 files (+84/-352)

## 391. feat(router): add total count for payments list (#1912)

- **Commit:** `7a5c8413`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-08-29T16:48:35+05:30
- **Changes:** 10 files (+292/-16)

## 392. feat(router): verify service for applepay merchant registration (#2009)

- **Commit:** `636b871b`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-08-31T13:20:06+05:30
- **Changes:** 11 files (+214/-0)

## 393. feat(connector): [Square] Implement Card Payments for Square (#1902)

- **Commit:** `c9fe389b`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-08-31T17:09:16+05:30
- **Changes:** 21 files (+1024/-207)

## 394. refactor(router): return generic message for UnprocessableEntity in make_pm_data (#2050)

- **Commit:** `38ab6e54`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-09-01T13:52:22+05:30
- **Changes:** 5 files (+342/-78)

## 395. feat(api): use `ApiClient` trait in AppState (#2067)

- **Commit:** `29fd2eaa`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-09-01T15:36:35+05:30
- **Changes:** 14 files (+216/-80)

## 396. refactor(connector): [Shift4] refactor connector authorize request struct  (#1888)

- **Commit:** `e44c32dd`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-09-01T19:41:57+05:30
- **Changes:** 2 files (+335/-116)

## 397. feat(pm_list): add card - credit pm type required field info for connectors (#2075)

- **Commit:** `a882d760`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-09-01T23:25:23+05:30
- **Changes:** 3 files (+1910/-131)

## 398. ci(postman): Fix Stripe collection to address check failure (#2078)

- **Commit:** `c5003aaa`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-09-04T17:44:29+05:30
- **Changes:** 55 files (+14357/-14189)

## 399. feat(frm): Add support to accept and decline payment when manually reviewed by merchant for risky transaction (#2071)

- **Commit:** `229f111f`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-09-04T17:44:39+05:30
- **Changes:** 36 files (+1382/-78)

## 400. feat(connector): [Payme] Implement Card 3DS with sdk flow (#2082)

- **Commit:** `99f1780f`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-09-05T20:53:59+05:30
- **Changes:** 10 files (+576/-74)

## 401. refactor(scheduler): move scheduler to new crate to support workflows in multiple crates (#1681)

- **Commit:** `d4221f33`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2023-09-06T13:11:09+05:30
- **Changes:** 72 files (+1966/-1124)

## 402. feat(payment_methods): Store necessary payment method data in payment_methods table (#2073)

- **Commit:** `3c935521`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2023-09-06T19:25:25+05:30
- **Changes:** 23 files (+204/-16)

## 403. feat(apple_pay): add support for pre decrypted apple pay token (#2056)

- **Commit:** `75ee6327`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-09-07T22:49:10+05:30
- **Changes:** 34 files (+1174/-227)

## 404. feat(connector): (checkout.com) add support for multiple captures PSync (#2043)

- **Commit:** `517c5c41`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-09-08T12:47:43+05:30
- **Changes:** 12 files (+259/-47)

## 405. feat(payments): make database calls parallel for `payments_confirm` operation (#2098)

- **Commit:** `fea075e3`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2023-09-08T18:28:07+05:30
- **Changes:** 2 files (+168/-129)

## 406. feat(core): accept payment_confirm_source header in capture call and store in payment_intent (#2116)

- **Commit:** `2f272d29`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-09-11T12:12:28+05:30
- **Changes:** 35 files (+207/-21)

## 407. refactor(core): use profile id to find connector (#2020)

- **Commit:** `5b29c252`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-09-11T12:55:22+05:30
- **Changes:** 37 files (+776/-363)

## 408. refactor(storage_impl): split payment attempt models to domain + diesel (#2010)

- **Commit:** `ad4b7de6`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-09-11T17:33:47+05:30
- **Changes:** 57 files (+2358/-1542)

## 409. feat(core): enable payments void for multiple partial capture (#2048)

- **Commit:** `a81bfe28`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-09-11T23:09:36+05:30
- **Changes:** 15 files (+230/-652)

## 410. feat(connector): [Braintree] implement 3DS card payment for braintree (#2095)

- **Commit:** `d63cbbd4`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-09-12T13:46:24+05:30
- **Changes:** 4 files (+652/-43)

## 411. fix(router/scheduler): replace the occurrences of gen_range with a safer alternative (#2126)

- **Commit:** `94ac5c03`
- **Author:** Anup Jadhav <anup.jadhav@gmail.com>
- **Date:** 2023-09-12T10:04:16+01:00
- **Changes:** 4 files (+657/-86)

## 412. fix(refactor): [Paypal] refactor paypal not implemented payment methods errors (#1974)

- **Commit:** `ca9fb0ca`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-09-12T15:31:44+05:30
- **Changes:** 1 files (+213/-5)

## 413. feat(router): added new webhook URL to support `merchant_connector_id` (#2006)

- **Commit:** `82b36e88`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-09-13T00:54:41+05:30
- **Changes:** 12 files (+160/-149)

## 414. refactor: move `Request` and `RequestBuilder` structs to common_utils crate (#2145)

- **Commit:** `21be67ad`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-09-13T16:05:26+05:30
- **Changes:** 7 files (+227/-213)

## 415. fix(router): Add scoped error enum for customer error (#1988)

- **Commit:** `5c5058de`
- **Author:** Jeeva <jeevaprakashdr@hotmail.com>
- **Date:** 2023-09-13T18:46:14+01:00
- **Changes:** 11 files (+203/-34)

## 416. refactor(connector): [BraintreeGraphQl] Enhance currency Mapping with ConnectorCurrencyCommon Trait  (#2143)

- **Commit:** `05696d32`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-09-14T13:05:46+05:30
- **Changes:** 6 files (+246/-66)

## 417. refactor(router): get route for applepay_verified_domains (#2157)

- **Commit:** `fb1760b1`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-09-14T17:20:37+05:30
- **Changes:** 7 files (+157/-89)

## 418. feat(connector): (adyen) add support for multiple partial capture adyen (#2102)

- **Commit:** `9668a74a`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-09-15T12:58:45+05:30
- **Changes:** 11 files (+308/-255)

## 419. refactor(connector): [Bluesnap] Enahnce 3ds Flow (#2115)

- **Commit:** `272f5e4c`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-09-16T23:46:11+05:30
- **Changes:** 8 files (+142/-167)

## 420. refactor(core): Add additional parameters in AppState and refactor AppState references (#2123)

- **Commit:** `a0a8ef27`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-09-18T14:01:03+05:30
- **Changes:** 46 files (+531/-395)

## 421. feat(connector): [Gocardless] add boilerplate code (#2179)

- **Commit:** `6a641806`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-09-18T15:10:07+05:30
- **Changes:** 17 files (+1249/-7)

## 422. feat(connector): [Gocardless] add support for Ach, Sepa, Becs payment methods (#2180)

- **Commit:** `3efce901`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-09-20T18:45:10+05:30
- **Changes:** 18 files (+1308/-280)

## 423. refactor(router): refactor customer <> address in customers and payments flow (#2158)

- **Commit:** `8ee2ce1f`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-09-20T19:27:45+05:30
- **Changes:** 28 files (+522/-329)

## 424. feat(core): add support for webhook additional source verification call for paypal (#2058)

- **Commit:** `2a9e09d8`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-09-20T19:28:02+05:30
- **Changes:** 13 files (+719/-77)

## 425. feat(router): add kv implementation for address for payment flows (#2177)

- **Commit:** `afff3e17`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-09-21T15:13:48+05:30
- **Changes:** 20 files (+418/-113)

## 426. refactor(connector): [Stripe] refactor stripe payment method not implemented errors (#1927)

- **Commit:** `417f7932`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-09-21T21:55:32+05:30
- **Changes:** 2 files (+516/-442)

## 427. refactor(connector): [Adyen] Enhance currency Mapping with ConnectorCurrencyCommon Trait  (#2209)

- **Commit:** `3d18f206`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-09-21T22:36:08+05:30
- **Changes:** 2 files (+286/-175)

## 428. feat(router): add mertics to apple pay flow (#2235)

- **Commit:** `b9f25c4a`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-09-22T16:06:15+05:30
- **Changes:** 12 files (+193/-38)

## 429. feat(payments): add api locking for payments core (#1898)

- **Commit:** `5d661561`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-09-25T15:55:39+05:30
- **Changes:** 44 files (+802/-158)

## 430. feat(connector_response): kv for connector response table (#2207)

- **Commit:** `cefa291c`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-09-25T20:31:13+05:30
- **Changes:** 8 files (+305/-62)

## 431. refactor(connector): [bluesnap]Enhance currency Mapping with ConnectorCurrencyCommon Trait (#2193)

- **Commit:** `6db60b8c`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-09-26T12:01:25+05:30
- **Changes:** 2 files (+261/-176)

## 432. ci(ui_test): Refactor core of UI tests to use injected browser data (#2178)

- **Commit:** `f47a5d42`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-09-26T17:43:02+05:30
- **Changes:** 10 files (+134/-67)

## 433. refactor(connector): [bluesnap] add refund status and webhooks (#2374)

- **Commit:** `fe43458d`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-09-27T17:35:44+05:30
- **Changes:** 2 files (+125/-95)

## 434. feat(router): add profile id and extra filters in lists (#2379)

- **Commit:** `ab2cde79`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-10-04T19:39:45+05:30
- **Changes:** 15 files (+226/-108)

## 435. refactor(router): renamed Verify flow to SetupMandate (#2455)

- **Commit:** `80f3b1ed`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-10-05T20:30:48+05:30
- **Changes:** 61 files (+458/-241)

## 436. feat(core): add surcharge_details field to ResponsePaymentMethodTypes struct (#2435)

- **Commit:** `3f0d927c`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-10-05T23:52:47+05:30
- **Changes:** 10 files (+417/-12)

## 437. feat(router): add mandates incoming webhooks flow (#2464)

- **Commit:** `1cf8b6cf`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-10-06T00:38:47+05:30
- **Changes:** 19 files (+321/-8)

## 438. feat(connector): [Gocardless] Implement mandate flow (#2461)

- **Commit:** `41499659`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-10-06T00:50:45+05:30
- **Changes:** 8 files (+183/-143)

## 439. refactor: add support for passing context generic to api calls (#2433)

- **Commit:** `601c1744`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-10-06T13:10:13+05:30
- **Changes:** 26 files (+702/-413)

## 440. feat(connector): [Braintree] implement dispute webhook  (#2031)

- **Commit:** `eeccd106`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-10-06T15:07:04+05:30
- **Changes:** 26 files (+375/-63)

## 441. feat(connector): [Paypal] Implement 3DS for Cards (#2443)

- **Commit:** `d95a64d6`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-10-06T16:54:20+05:30
- **Changes:** 2 files (+242/-25)

## 442. feat(process_tracker): make long standing payments failed (#2380)

- **Commit:** `73dfc31f`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-10-09T14:32:46+05:30
- **Changes:** 7 files (+268/-83)

## 443. feat(kv): add kv wrapper for executing kv tasks (#2384)

- **Commit:** `8b50997e`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-10-09T18:40:58+05:30
- **Changes:** 18 files (+547/-186)

## 444. feat: kv for reverse lookup (#2445)

- **Commit:** `13aaf96d`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-10-10T14:35:00+05:30
- **Changes:** 16 files (+453/-163)

## 445. refactor(test_utils): Refactor `test_utils` crate and add `folder` support with updated documentation (#2487)

- **Commit:** `6b52ac3d`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2023-10-10T15:59:57+05:30
- **Changes:** 4 files (+197/-155)

## 446. feat(connector): [Volt] Template generation (#2480)

- **Commit:** `ee321bb8`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-10-11T12:27:28+05:30
- **Changes:** 16 files (+1230/-12)

## 447. feat(router): add kv implementation for update address in update payments flow (#2542)

- **Commit:** `9f446bc1`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-10-12T12:12:51+05:30
- **Changes:** 8 files (+203/-8)

## 448. fix: percentage float inconsistency problem and api models changes to support surcharge feature (#2550)

- **Commit:** `1ee11849`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-10-12T13:06:09+05:30
- **Changes:** 35 files (+390/-47)

## 449. feat(router): Add payment link support (#2105)

- **Commit:** `642085dc`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-10-12T14:39:10+05:30
- **Changes:** 58 files (+2565/-23)

## 450. fix(connector): [braintree] add 3ds redirection error mapping and metadata validation (#2552)

- **Commit:** `28d02f94`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-10-12T19:05:37+05:30
- **Changes:** 5 files (+150/-71)

## 451. feat(customers): add customer list endpoint (#2564)

- **Commit:** `c26620e0`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-10-12T19:58:34+05:30
- **Changes:** 12 files (+207/-24)

## 452. fix(connector): Trigger Psync after redirection url (#2422)

- **Commit:** `8029a895`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-10-12T20:14:53+05:30
- **Changes:** 13 files (+98/-116)

## 453. refactor(storage): update paymentintent object to provide a relation with attempts (#2502)

- **Commit:** `fbf3c03d`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-10-13T08:10:54+05:30
- **Changes:** 36 files (+875/-856)

## 454. feat(connector): [HELCIM] Implement Cards for Helcim (#2210)

- **Commit:** `b5feab61`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-10-13T18:14:12+05:30
- **Changes:** 17 files (+1205/-130)

## 455. feat(router): Better UI payment link and order details product image and merchant config support (#2583)

- **Commit:** `fdd95800`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-10-17T14:40:45+05:30
- **Changes:** 19 files (+468/-204)

## 456. fix: make push to drainer generic and add application metrics for KV (#2563)

- **Commit:** `274a7834`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-10-17T11:21:18+00:00
- **Changes:** 11 files (+258/-334)

## 457. feat: add updated_by to tracker tables (#2604)

- **Commit:** `6a74e8cb`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-10-17T11:26:56+00:00
- **Changes:** 46 files (+549/-176)

## 458. fix(connector): [Authorizedotnet]fix error deserialization incase of authentication failure (#2600)

- **Commit:** `4859b7da`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-10-17T20:05:29+05:30
- **Changes:** 23 files (+633/-25)

## 459. feat(merchant_account): add merchant account list endpoint  (#2560)

- **Commit:** `a1472c6b`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-10-18T12:53:18+05:30
- **Changes:** 13 files (+244/-3)

## 460. feat: update surcharge_amount and tax_amount in update_trackers of payment_confirm (#2603)

- **Commit:** `2f9a3557`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-10-18T15:42:32+05:30
- **Changes:** 31 files (+786/-47)

## 461. refactor(router): remove unnecessary function from Refunds Validate Flow (#2609)

- **Commit:** `3399328a`
- **Author:** Aaron Jackson <AaronTJDev@gmail.com>
- **Date:** 2023-10-18T03:35:05-07:00
- **Changes:** 2 files (+71/-129)

## 462. feat(Connector): [Paypal] add support for dispute webhooks for paypal connector (#2353)

- **Commit:** `6cf8f058`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-10-18T16:54:56+05:30
- **Changes:** 2 files (+191/-9)

## 463. feat(core): replace temp locker with redis (#2594)

- **Commit:** `2edbd612`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-10-18T19:04:26+05:30
- **Changes:** 13 files (+213/-551)

## 464. feat(connector): [ProphetPay] Template generation (#2610)

- **Commit:** `7e6207e6`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-10-19T13:20:40+05:30
- **Changes:** 16 files (+1226/-6)

## 465. refactor: revert redis temp locker logic (#2670)

- **Commit:** `eaa97205`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-10-23T20:18:47+05:30
- **Changes:** 20 files (+594/-249)

## 466. feat(core): add support for multiple `merchant_connector_account`  (#2655)

- **Commit:** `5988d8d4`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-10-25T21:27:24+05:30
- **Changes:** 87 files (+393/-137)

## 467. feat(events): add masked json serializer for logging PII values (#2681)

- **Commit:** `13c66df9`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-10-27T12:58:09+05:30
- **Changes:** 20 files (+518/-48)

## 468. fix(connector): [Forte] Response Handling for Verify Action (#2601)

- **Commit:** `efed5968`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-10-27T15:10:16+05:30
- **Changes:** 11 files (+276/-0)

## 469. feat(connector): [VOLT] Implement payment flows and bank redirect payment method (#2582)

- **Commit:** `23bd364a`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-10-30T13:13:28+05:30
- **Changes:** 94 files (+2970/-146)

## 470. feat(organization): add organization table (#2669)

- **Commit:** `d6824710`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-10-30T14:24:28+05:30
- **Changes:** 15 files (+282/-4)

## 471. refactor(db): migrate to payment_attempt from connector_response  (#2656)

- **Commit:** `9d9fc2a8`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-10-31T00:04:53+05:30
- **Changes:** 9 files (+259/-30)

## 472. fix(connector): [Stripe] add decline_code in error_reason (#2735)

- **Commit:** `0a44f569`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-10-31T17:37:04+05:30
- **Changes:** 11 files (+462/-14)

## 473. feat(connector): [Multisafepay] add error handling (#2595)

- **Commit:** `b3c846d6`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-11-02T12:47:25+05:30
- **Changes:** 11 files (+448/-76)

## 474. feat(analytics): analytics APIs (#2676)

- **Commit:** `c0a5e7b7`
- **Author:** ivor-juspay <138492857+ivor-juspay@users.noreply.github.com>
- **Date:** 2023-11-03T12:01:47+05:30
- **Changes:** 47 files (+4507/-13)

## 475. revert: fix(analytics): feat(analytics): analytics APIs (#2777)

- **Commit:** `169d33bf`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-11-03T17:29:32+05:30
- **Changes:** 47 files (+13/-4507)

## 476. feat(router): Add Smart Routing to route payments efficiently (#2665)

- **Commit:** `9b618d24`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-11-03T18:37:31+05:30
- **Changes:** 96 files (+15366/-223)

## 477. feat(connector): [BANKOFAMERICA] Add Connector Template Code (#2764)

- **Commit:** `45639353`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-11-06T13:46:12+05:30
- **Changes:** 18 files (+1262/-13)

## 478. feat(core): use redis as temp locker instead of basilisk (#2789)

- **Commit:** `66786892`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-11-08T13:12:28+05:30
- **Changes:** 23 files (+554/-531)

## 479. refactor(router): add parameter connectors to get_request_body function (#2708)

- **Commit:** `7623ea93`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-11-08T15:49:49+05:30
- **Changes:** 53 files (+920/-259)

## 480. feat(router): add `gateway_status_map` interface (#2804)

- **Commit:** `a429b23c`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-08T15:54:50+05:30
- **Changes:** 11 files (+436/-4)

## 481. feat(events): add extracted fields based on req/res types (#2795)

- **Commit:** `89857941`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-11-08T21:31:53+05:30
- **Changes:** 40 files (+664/-69)

## 482. feat(router): add `gateway_status_map` CRUD APIs (#2809)

- **Commit:** `5c9e235b`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-09T18:13:38+05:30
- **Changes:** 16 files (+402/-4)

## 483. refactor(core): remove connector response table and use payment_attempt instead (#2644)

- **Commit:** `966369b6`
- **Author:** Abhishek Marrivagu <68317979+Abhicodes-crypto@users.noreply.github.com>
- **Date:** 2023-11-09T20:39:12+05:30
- **Changes:** 35 files (+155/-979)

## 484. feat(user): setup user tables (#2803)

- **Commit:** `20c4226a`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-11-10T11:47:32+05:30
- **Changes:** 19 files (+919/-1)

## 485. feat(router): added Payment link new design (#2731)

- **Commit:** `2a4f5d13`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-11-10T14:39:32+05:30
- **Changes:** 7 files (+737/-667)

## 486. feat(analytics): analytics APIs  (#2792)

- **Commit:** `f8478023`
- **Author:** ivor-juspay <138492857+ivor-juspay@users.noreply.github.com>
- **Date:** 2023-11-10T17:08:09+05:30
- **Changes:** 47 files (+4559/-14)

## 487. feat(router): Add new JWT authentication variants and use them (#2835)

- **Commit:** `f88eee73`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-11-13T11:17:35+05:30
- **Changes:** 34 files (+3489/-67)

## 488. feat(router): profile specific fallback derivation while routing payments (#2806)

- **Commit:** `8e538dbd`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-11-13T14:57:34+05:30
- **Changes:** 8 files (+312/-34)

## 489. build(deps): remove unused dependencies and features (#2854)

- **Commit:** `05535871`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-11-13T16:50:18+05:30
- **Changes:** 28 files (+86/-156)

## 490. feat(router): add automatic retries and step up 3ds flow (#2834)

- **Commit:** `d2968c94`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-13T22:19:37+05:30
- **Changes:** 4 files (+619/-3)

## 491. fix: handle session and confirm flow discrepancy in surcharge details (#2696)

- **Commit:** `cafea459`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-11-14T16:11:38+05:30
- **Changes:** 20 files (+477/-77)

## 492. feat: change async-bb8 fork and tokio spawn for concurrent database calls (#2774)

- **Commit:** `d634fdea`
- **Author:** Arun Raj M <jarnura47@gmail.com>
- **Date:** 2023-11-16T10:27:34+05:30
- **Changes:** 69 files (+1512/-717)

## 493. refactor(router): add openapi spec support for gsm apis (#2871)

- **Commit:** `62c9ccae`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-16T18:48:42+05:30
- **Changes:** 8 files (+515/-18)

## 494. feat(router): add api to migrate card from basilisk to rust (#2853)

- **Commit:** `b8b20c41`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-11-16T19:02:54+05:30
- **Changes:** 24 files (+274/-20)

## 495. feat(connector): [BANKOFAMERICA] Implement Cards for Bank of America (#2765)

- **Commit:** `e8de3a71`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-11-16T19:40:53+05:30
- **Changes:** 178 files (+10152/-207)

## 496. feat(connector): [ProphetPay] Implement Card Redirect PaymentMethodType and flows for Authorize, CompleteAuthorize, Psync, Refund, Rsync and Void (#2641)

- **Commit:** `8d4adc52`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-11-16T20:42:08+05:30
- **Changes:** 29 files (+722/-151)

## 497. feat(router): add fallback while add card and retrieve card from rust locker (#2888)

- **Commit:** `f735fb05`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2023-11-16T22:54:14+05:30
- **Changes:** 7 files (+208/-131)

## 498. fix(core): introduce new attempt and intent status to handle multiple partial captures (#2802)

- **Commit:** `cb88be01`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-11-17T10:04:34+05:30
- **Changes:** 46 files (+600/-59)

## 499. feat(events): add incoming webhook payload to api events logger (#2852)

- **Commit:** `aea390a6`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-11-17T13:38:23+05:30
- **Changes:** 65 files (+259/-202)

## 500. fix(router): associate parent payment token with `payment_method_id` as hyperswitch token for saved cards (#2130)

- **Commit:** `efeebc0f`
- **Author:** Shanks <shashank.attarde@juspay.in>
- **Date:** 2023-11-20T16:12:06+05:30
- **Changes:** 6 files (+320/-102)

## 501. feat(router): add unified_code, unified_message in payments response (#2918)

- **Commit:** `39540015`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-20T17:35:07+05:30
- **Changes:** 20 files (+242/-45)

## 502. refactor(core): query business profile only once (#2830)

- **Commit:** `44deeb7e`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-11-20T18:19:19+05:30
- **Changes:** 13 files (+772/-579)

## 503. refactor: add mapping for ConnectorError in payouts flow (#2608)

- **Commit:** `5c4e7c90`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2023-11-21T13:04:22+05:30
- **Changes:** 96 files (+2310/-62)

## 504. refactor(connector): [Paypal] Add support for both BodyKey and SignatureKey (#2633)

- **Commit:** `d8fcd3c9`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2023-11-21T19:44:40+05:30
- **Changes:** 2 files (+325/-56)

## 505. feat: add support for 3ds and surcharge decision through routing rules (#2869)

- **Commit:** `f8618e07`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-11-21T20:25:50+05:30
- **Changes:** 23 files (+1717/-58)

## 506. feat(connector): [Prophetpay] Save card token for Refund and remove Void flow (#2927)

- **Commit:** `15a255ea`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-11-21T21:22:50+05:30
- **Changes:** 2 files (+272/-159)

## 507. fix:  cybersource mandates and fiserv exp year (#2920)

- **Commit:** `7f74ae98`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2023-11-22T00:35:40+05:30
- **Changes:** 5 files (+427/-126)

## 508. feat(router): add list payment link support (#2805)

- **Commit:** `b441a1f2`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2023-11-22T15:37:01+05:30
- **Changes:** 23 files (+330/-44)

## 509. refactor(macros): use syn2.0  (#2890)

- **Commit:** `46e13d54`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-11-22T15:46:33+05:30
- **Changes:** 26 files (+495/-359)

## 510. feat(connector): [BANKOFAMERICA] Implement Google Pay (#2940)

- **Commit:** `f91d4ae1`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-11-22T22:01:07+05:30
- **Changes:** 1 files (+210/-46)

## 511. feat(auth): Add Authorization for JWT Authentication types (#2973)

- **Commit:** `03c0a772`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-11-24T19:11:46+05:30
- **Changes:** 20 files (+659/-91)

## 512. feat(currency_conversion): add currency conversion feature (#2948)

- **Commit:** `c0116db2`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2023-11-28T16:05:04+05:30
- **Changes:** 27 files (+1501/-10)

## 513. feat(payment_methods): receive `card_holder_name` in confirm flow when using token for payment (#2982)

- **Commit:** `e7ad3a4d`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-11-28T16:22:33+05:30
- **Changes:** 40 files (+375/-237)

## 514. feat(core): [Paypal] Add Preprocessing flow to CompleteAuthorize for Card 3DS Auth Verification (#2757)

- **Commit:** `77fc92c9`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-11-28T16:40:42+05:30
- **Changes:** 9 files (+338/-3)

## 515. fix(connector): [Adyen] `ErrorHandling` in case of Balance Check for Gift Cards (#1976)

- **Commit:** `bd889c83`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-11-28T17:32:53+05:30
- **Changes:** 26 files (+660/-120)

## 516. refactor(router): add openapi spec support for merchant_connector apis (#2997)

- **Commit:** `cdbb3853`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-28T19:17:17+05:30
- **Changes:** 3 files (+259/-6)

## 517. fix(core): Replace euclid enum with RoutableConnectors enum (#2994)

- **Commit:** `ff6a0dd0`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-11-28T20:34:30+05:30
- **Changes:** 18 files (+147/-443)

## 518. fix: few fields were not getting updated in apply_changeset function (#3002)

- **Commit:** `d2895248`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-11-29T13:54:16+05:30
- **Changes:** 5 files (+190/-123)

## 519. feat(ses_email): add email services to hyperswitch (#2977)

- **Commit:** `5f5e895f`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2023-11-29T16:12:12+05:30
- **Changes:** 18 files (+1857/-93)

## 520. feat(analytics): Add Clickhouse based analytics (#2988)

- **Commit:** `9df4e019`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-11-29T17:04:53+05:30
- **Changes:** 135 files (+12141/-897)

## 521. feat(core): Add ability to verify connector credentials before integrating the connector (#2986)

- **Commit:** `39f255b4`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-11-30T13:06:35+05:30
- **Changes:** 18 files (+552/-2)

## 522. feat(user): add support for dashboard metadata (#3000)

- **Commit:** `6a2e4ab4`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-11-30T14:58:37+05:30
- **Changes:** 28 files (+1389/-16)

## 523. feat(connector): [BANKOFAMERICA] Add Required Fields for GPAY (#3014)

- **Commit:** `d30b58ab`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-11-30T15:31:01+05:30
- **Changes:** 1 files (+210/-9)

## 524. feat(router): make core changes in payments flow to support incremental authorization (#3009)

- **Commit:** `1ca2ba45`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-11-30T16:56:34+05:30
- **Changes:** 88 files (+363/-11)

## 525. feat(user_role): Add APIs for user roles (#3013)

- **Commit:** `3fa0bdf7`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-11-30T20:02:47+05:30
- **Changes:** 24 files (+1207/-46)

## 526. feat(user): generate and delete sample data (#2987)

- **Commit:** `092ec73b`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-12-01T16:00:25+05:30
- **Changes:** 22 files (+1151/-18)

## 527. feat(user): add user_list and switch_list apis (#3033)

- **Commit:** `ec15ddd0`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-12-01T19:07:17+05:30
- **Changes:** 16 files (+356/-52)

## 528. refactor(users): Separate signup and signin (#2921)

- **Commit:** `80efeb76`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-12-04T17:03:44+05:30
- **Changes:** 9 files (+453/-109)

## 529. refactor: create separate struct for surcharge details response (#3027)

- **Commit:** `57591f81`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-12-04T17:11:30+05:30
- **Changes:** 14 files (+325/-217)

## 530. feat(router): add payments incremental authorization api (#3038)

- **Commit:** `a0cfdd3f`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2023-12-04T18:34:51+05:30
- **Changes:** 60 files (+1792/-22)

## 531. fix: use card bin to get additional card details (#3036)

- **Commit:** `6c7d3a2e`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-12-04T19:51:41+05:30
- **Changes:** 9 files (+125/-103)

## 532. feat: calculate surcharge for customer saved card list (#3039)

- **Commit:** `daf0f09f`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-12-04T22:30:51+05:30
- **Changes:** 15 files (+477/-287)

## 533. fix: add fallback to reverselookup error (#3025)

- **Commit:** `ba392f58`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-12-05T12:47:37+05:30
- **Changes:** 14 files (+288/-227)

## 534. feat(user): add email apis and new enums for metadata (#3053)

- **Commit:** `1c3d260d`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2023-12-05T13:10:17+05:30
- **Changes:** 19 files (+728/-54)

## 535. feat(connector_onboarding): Add Connector onboarding APIs (#3050)

- **Commit:** `7bd6e05c`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2023-12-05T15:29:10+05:30
- **Changes:** 25 files (+876/-6)

## 536. feat: implement FRM flows (#2968)

- **Commit:** `055d8383`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2023-12-05T18:21:32+05:30
- **Changes:** 45 files (+5188/-150)

## 537. feat(connector): [BANKOFAMERICA] Implement Apple Pay (#3061)

- **Commit:** `47c03830`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-06T15:26:38+05:30
- **Changes:** 5 files (+205/-45)

## 538. feat(pm_auth): pm_auth service migration (#3047)

- **Commit:** `9c1c44a7`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-12-06T20:48:41+05:30
- **Changes:** 40 files (+2492/-25)

## 539. refactor(payment_methods): make the card_holder_name optional for card details in the payment APIs (#3074)

- **Commit:** `b2795910`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2023-12-08T17:58:42+05:30
- **Changes:** 39 files (+170/-78)

## 540. feat: add utility to convert TOML configuration file to list of environment variables (#3096)

- **Commit:** `2c4599a1`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2023-12-11T13:20:19+05:30
- **Changes:** 30 files (+498/-479)

## 541. chore(deps): update fred and moka (#3088)

- **Commit:** `129b1e55`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2023-12-11T15:21:23+05:30
- **Changes:** 14 files (+130/-129)

## 542. feat(connector): [Placetopay] Add Connector Template Code  (#3084)

- **Commit:** `a7b688aa`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-12-12T15:03:21+05:30
- **Changes:** 21 files (+1256/-7)

## 543. feat(connector): [RISKIFIED] Add support for riskified frm connector (#2533)

- **Commit:** `151a30f4`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-12-12T18:39:36+05:30
- **Changes:** 58 files (+1646/-61)

## 544. feat(events): add type info to outgoing requests & maintain structural & PII type info (#2956)

- **Commit:** `6e82b0bd`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2023-12-13T11:26:03+05:30
- **Changes:** 93 files (+1496/-2555)

## 545. feat(connector): [HELCIM] Add connector_request_reference_id in invoice_number  (#3087)

- **Commit:** `3cc9642f`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-13T12:54:08+05:30
- **Changes:** 5 files (+237/-9)

## 546. fix: validate refund amount with amount_captured instead of amount (#3120)

- **Commit:** `be13d15d`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-12-13T19:22:36+05:30
- **Changes:** 31 files (+538/-24)

## 547. feat(core): enable surcharge support for all connectors (#3109)

- **Commit:** `57e1ae9d`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2023-12-14T11:38:14+05:30
- **Changes:** 25 files (+131/-72)

## 548. fix(connector): [Checkout] Fix status mapping for checkout (#3073)

- **Commit:** `5b2c3291`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2023-12-15T16:35:41+05:30
- **Changes:** 185 files (+14869/-14202)

## 549. feat(connector): [CYBERSOURCE] Implement Google Pay (#3139)

- **Commit:** `4ae6af46`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-15T17:07:55+05:30
- **Changes:** 2 files (+349/-83)

## 550. fix: [CYBERSOURCE] Fix Status Mapping (#3144)

- **Commit:** `62c0c47e`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-17T12:42:11+05:30
- **Changes:** 2 files (+359/-168)

## 551. feat(connector): [PlaceToPay] Implement Cards for PlaceToPay (#3117)

- **Commit:** `107c66fe`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2023-12-17T13:25:53+05:30
- **Changes:** 7 files (+482/-130)

## 552. feat(connector): [NMI] Implement 3DS for Cards (#3143)

- **Commit:** `7df45235`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-12-17T14:38:37+05:30
- **Changes:** 5 files (+556/-11)

## 553. fix(connector): [BOA/CYBERSOURCE] Update error handling (#3156)

- **Commit:** `8e484dda`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-18T15:59:00+05:30
- **Changes:** 4 files (+146/-123)

## 554. fix(connector): Connector wise validation for zero auth flow (#3159)

- **Commit:** `45ba128b`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2023-12-19T19:00:22+05:30
- **Changes:** 50 files (+696/-29)

## 555. feat(connector): [NMI] Implement webhook for Payments and Refunds (#3164)

- **Commit:** `30c14019`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2023-12-19T20:11:31+05:30
- **Changes:** 2 files (+272/-29)

## 556. feat(connector-config): add wasm support for dashboard connector configuration (#3138)

- **Commit:** `b0ffbe93`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2023-12-19T22:52:06+05:30
- **Changes:** 13 files (+3292/-3)

## 557. fix(connector): [BOA] Display 2XX Failure Errors (#3200)

- **Commit:** `07fd9bed`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-22T19:38:58+05:30
- **Changes:** 1 files (+172/-83)

## 558. fix(connector): [CYBERSOURCE] Display 2XX Failure Errors (#3201)

- **Commit:** `86c26221`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-22T20:16:58+05:30
- **Changes:** 1 files (+157/-76)

## 559. feat(connector): [CYBERSOURCE] Refactor cybersource (#3215)

- **Commit:** `e06ba148`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2023-12-29T14:23:31+05:30
- **Changes:** 2 files (+267/-19)

## 560. fix(core): fix recurring mandates flow for cyber source (#3224)

- **Commit:** `6a1743eb`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-01-03T18:58:10+05:30
- **Changes:** 3 files (+219/-135)

## 561. refactor: address panics due to indexing and slicing (#3233)

- **Commit:** `34318bc1`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-01-05T14:47:37+05:30
- **Changes:** 39 files (+244/-253)

## 562. feat(analytics): adding outgoing webhooks kafka event (#3140)

- **Commit:** `1d26df28`
- **Author:** harsh-sharma-juspay <125131007+harsh-sharma-juspay@users.noreply.github.com>
- **Date:** 2024-01-05T16:01:56+05:30
- **Changes:** 9 files (+268/-11)

## 563. feat: add deep health check (#3210)

- **Commit:** `f30ba898`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-01-05T16:21:40+05:30
- **Changes:** 11 files (+304/-4)

## 564. chore: address Rust 1.75 clippy lints (#3231)

- **Commit:** `c8279b11`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-01-05T16:22:31+05:30
- **Changes:** 25 files (+141/-142)

## 565. fix(analytics): added response to the connector outgoing event (#3129)

- **Commit:** `d152c3a1`
- **Author:** Sagar naik <sagar.naik@juspay.in>
- **Date:** 2024-01-05T18:58:55+05:30
- **Changes:** 8 files (+145/-149)

## 566. refactor(euclid_wasm): Update wasm config (#3222)

- **Commit:** `7ea50c3a`
- **Author:** Jeeva Ramachandran <120017870+JeevaRamu0104@users.noreply.github.com>
- **Date:** 2024-01-08T11:25:05+05:30
- **Changes:** 7 files (+5682/-962)

## 567. feat(pm_list): add required fields for eps (#3169)

- **Commit:** `bfd8a5a3`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-01-08T16:57:54+05:30
- **Changes:** 10 files (+46352/-45290)

## 568. fix(router): Payment link api contract change (#2975)

- **Commit:** `3cd74966`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-01-08T17:40:56+05:30
- **Changes:** 44 files (+1651/-812)

## 569. refactor(drainer): change logic for trimming the stream and refactor for modularity (#3128)

- **Commit:** `de7a607e`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-01-08T18:12:13+05:30
- **Changes:** 12 files (+636/-486)

## 570. feat(connector): Add Revoke mandate flow (#3261)

- **Commit:** `90ac26a9`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-01-08T19:11:16+05:30
- **Changes:** 11 files (+472/-21)

## 571. fix(connector): [BOA, Cybersource] capture error_code (#3239)

- **Commit:** `ecf51b5e`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-01-09T12:31:39+05:30
- **Changes:** 3 files (+220/-205)

## 572. feat(Connector): [VOLT] Add support for Payments Webhooks (#3155)

- **Commit:** `eba78964`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-01-09T19:54:54+05:30
- **Changes:** 2 files (+279/-31)

## 573. feat(pm_list): add required fields for Ideal  (#3183)

- **Commit:** `1c3c5f6b`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-01-09T20:44:19+05:30
- **Changes:** 16 files (+1669/-571)

## 574. feat(payment_link): add status page for payment link (#3213)

- **Commit:** `50e4d797`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-01-10T13:52:37+05:30
- **Changes:** 10 files (+642/-133)

## 575. refactor: removed basilisk feature (#3281)

- **Commit:** `612f8d9d`
- **Author:** Venkatesh <inventvenkat@gmail.com>
- **Date:** 2024-01-10T15:51:50+05:30
- **Changes:** 9 files (+1/-309)

## 576. feat(router): payment_method block (#3056)

- **Commit:** `bb096138`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-01-11T17:58:29+05:30
- **Changes:** 60 files (+1649/-38)

## 577. feat(connector): [BOA/CYB] Store AVS response in connector_metadata (#3271)

- **Commit:** `e75b11e9`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-01-11T19:16:16+05:30
- **Changes:** 4 files (+233/-119)

## 578. feat(connector): [cybersource] Implement 3DS flow for cards (#3290)

- **Commit:** `6fb3b00e`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-01-11T20:50:45+05:30
- **Changes:** 13 files (+1175/-44)

## 579. fix: update amount_capturable based on intent_status and payment flow (#3278)

- **Commit:** `469ea202`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-01-11T21:00:58+05:30
- **Changes:** 3 files (+192/-46)

## 580. chore: add api reference for blocklist (#3336)

- **Commit:** `f381d86b`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-01-12T18:28:57+05:30
- **Changes:** 7 files (+319/-32)

## 581. fix(connector_onboarding): Check if connector exists for the merchant account and add reset tracking id API (#3229)

- **Commit:** `58cc8d61`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-01-16T13:06:47+05:30
- **Changes:** 10 files (+186/-28)

## 582. feat(recon): add recon APIs (#3345)

- **Commit:** `8678f8d1`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-01-16T16:37:44+05:30
- **Changes:** 22 files (+639/-7)

## 583. feat(connector): [BANKOFAMERICA] Implement 3DS flow for cards (#3343)

- **Commit:** `d533c98b`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-01-16T17:59:22+05:30
- **Changes:** 8 files (+1017/-16)

## 584. feat(payment_method): add capability to store bank details using /payment_methods endpoint (#3113)

- **Commit:** `01c2de22`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-01-17T14:35:13+05:30
- **Changes:** 14 files (+412/-173)

## 585. refactor(connector): [cybersource] recurring mandate flow (#3354)

- **Commit:** `387c1c49`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-01-17T15:28:49+05:30
- **Changes:** 3 files (+170/-132)

## 586. refactor(core): add locker config to enable or disable locker  (#3352)

- **Commit:** `bd5356e7`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-01-18T18:10:21+05:30
- **Changes:** 23 files (+505/-98)

## 587. feat(users): Added get role from jwt api (#3385)

- **Commit:** `7516a167`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-01-18T20:18:44+05:30
- **Changes:** 10 files (+140/-111)

## 588. fix(frm): update FRM manual review flow (#3176)

- **Commit:** `5255ba91`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-01-19T12:14:33+05:30
- **Changes:** 7 files (+261/-394)

## 589. feat(hashicorp): implement hashicorp secrets manager solution (#3297)

- **Commit:** `629d546a`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2024-01-24T14:06:52+05:30
- **Changes:** 28 files (+1094/-84)

## 590. refactor(connector): [Iatapay] refactor authorize flow and fix payment status mapping (#2409)

- **Commit:** `f0c7bb9a`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2024-01-25T12:35:55+05:30
- **Changes:** 2 files (+203/-71)

## 591. feat(user): add support to delete user (#3374)

- **Commit:** `77777104`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-01-25T12:37:35+05:30
- **Changes:** 14 files (+271/-21)

## 592. fix(core): return surcharge in payment method list response if passed in create request (#3363)

- **Commit:** `3507ad60`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-01-25T12:38:50+05:30
- **Changes:** 4 files (+249/-197)

## 593. feat(connector): [Adyen] Add support for PIX Payment Method (#3236)

- **Commit:** `fc6e68f7`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-01-25T12:41:54+05:30
- **Changes:** 7 files (+196/-106)

## 594. feat(user): support multiple invites (#3422)

- **Commit:** `a59ac7d5`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-01-25T18:54:13+05:30
- **Changes:** 7 files (+296/-69)

## 595. refactor(openapi): move openapi to separate crate to decrease compile times (#3110)

- **Commit:** `7d8d68fa`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-01-29T16:20:43+05:30
- **Changes:** 48 files (+12652/-7229)

## 596. feat(core): update card_details for an existing mandate (#3452)

- **Commit:** `02074dfc`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-01-30T12:35:42+05:30
- **Changes:** 22 files (+451/-72)

## 597. feat(users): Signin and Verify Email changes for User Invitation changes (#3420)

- **Commit:** `d91da890`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-01-30T12:43:13+05:30
- **Changes:** 12 files (+369/-41)

## 598. refactor: add support for extending file storage to other schemes and provide a runtime flag for the same (#3348)

- **Commit:** `a9638d11`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-01-30T13:16:03+05:30
- **Changes:** 18 files (+461/-258)

## 599. refactor(settings): make the function to deserialize hashsets more generic (#3104)

- **Commit:** `87191d68`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-01-30T14:25:59+05:30
- **Changes:** 13 files (+391/-252)

## 600. feat(pm_list): add required fields for sofort (#3192)

- **Commit:** `3d55e3ba`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-01-30T14:26:55+05:30
- **Changes:** 11 files (+381/-65)

## 601. refactor(payment_link): segregated payment link in html css js files, sdk over flow issue, surcharge bug, block SPM customer call for payment link (#3410)

- **Commit:** `a7bc8c65`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-01-30T16:12:01+05:30
- **Changes:** 16 files (+2743/-2509)

## 602. refactor(core): restrict requires_customer_action in confirm (#3235)

- **Commit:** `d2accdef`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-01-30T17:16:02+05:30
- **Changes:** 18 files (+51/-410)

## 603. feat(users): Added blacklist for users (#3469)

- **Commit:** `e331d2d5`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-01-31T12:49:09+05:30
- **Changes:** 9 files (+169/-45)

## 604. feat: add deep health check for analytics (#3438)

- **Commit:** `7597f3b6`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-01-31T07:31:15+00:00
- **Changes:** 21 files (+282/-174)

## 605. feat(dashboard_metadata): Add email alert for Prod Intent (#3482)

- **Commit:** `94cd7b68`
- **Author:** Pritish Budhiraja <1805317@kiit.ac.in>
- **Date:** 2024-01-31T17:30:02+05:30
- **Changes:** 5 files (+250/-6)

## 606. refactor: rename `kms` feature flag to `aws_kms` (#3249)

- **Commit:** `91519d84`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-02T15:48:29+05:30
- **Changes:** 40 files (+507/-486)

## 607. feat: add deep health check for drainer (#3396)

- **Commit:** `63c383f5`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-02T16:29:35+05:30
- **Changes:** 9 files (+396/-3)

## 608. fix(connector): [Stripe] capture error message and error code for failed payment, capture, void and refunds (#3237)

- **Commit:** `2c52b377`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-02-06T16:19:13+05:30
- **Changes:** 1 files (+165/-52)

## 609. refactor(blocklist): separate utility function & kill switch for validating data in blocklist (#3360)

- **Commit:** `0a97a1eb`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-02-06T19:06:47+05:30
- **Changes:** 20 files (+557/-211)

## 610. feat(payouts): Add Wallet to Payouts (#3502)

- **Commit:** `3af6aaf2`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-02-07T12:21:57+05:30
- **Changes:** 23 files (+427/-102)

## 611. feat(core): add config for update_mandate_flow  (#3542)

- **Commit:** `14c0a2b0`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-02-07T23:23:14+05:30
- **Changes:** 13 files (+231/-93)

## 612. refactor(user_role): Change update user role request to take `email` instead of `user_id` (#3530)

- **Commit:** `edd6806f`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-02-08T14:19:44+05:30
- **Changes:** 10 files (+171/-75)

## 613. refactor(payment_methods): handle card duplication (#3146)

- **Commit:** `dd5630f0`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-08T17:40:52+05:30
- **Changes:** 3 files (+384/-89)

## 614. fix(core): Add column mandate_data for storing the details of a mandate in PaymentAttempt (#3606)

- **Commit:** `74f3721c`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-02-09T14:05:54+05:30
- **Changes:** 14 files (+91/-144)

## 615. feat(users): Add transfer org ownership API (#3603)

- **Commit:** `b9c29e7f`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-02-09T17:28:17+05:30
- **Changes:** 10 files (+341/-6)

## 616. feat(pm_list): add required fields for giropay  (#3194)

- **Commit:** `33df3520`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-02-12T13:26:05+05:30
- **Changes:** 14 files (+266/-19)

## 617. refactor: introducing `hyperswitch_interface` crates (#3536)

- **Commit:** `b6754a7d`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-12T13:30:44+05:30
- **Changes:** 44 files (+1157/-628)

## 618. feat(events): Connector response masking in clickhouse (#3566)

- **Commit:** `5fb3c001`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-02-14T12:04:26+05:30
- **Changes:** 129 files (+3200/-3238)

## 619. refactor: incorporate `hyperswitch_interface` into drainer (#3629)

- **Commit:** `7b1c65b6`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-14T15:12:01+05:30
- **Changes:** 11 files (+156/-81)

## 620. feat(connector): [Adyen] add PMD validation in validate_capture_method method for all the implemented PM’s (#3584)

- **Commit:** `0c46f39b`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-02-14T16:35:55+05:30
- **Changes:** 42 files (+195/-12)

## 621. feat(analytics): adding kafka dispute analytic events (#3549)

- **Commit:** `39e22339`
- **Author:** harsh-sharma-juspay <125131007+harsh-sharma-juspay@users.noreply.github.com>
- **Date:** 2024-02-16T18:06:07+05:30
- **Changes:** 8 files (+393/-4)

## 622. refactor: include api key expiry workflow into process tracker (#3661)

- **Commit:** `0a7625ff`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-19T13:33:17+05:30
- **Changes:** 11 files (+293/-36)

## 623. refactor(ext_traits): simplify the signatures of some methods in `Encode` extension trait (#3687)

- **Commit:** `11fc9b39`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-02-19T15:24:09+05:30
- **Changes:** 44 files (+392/-416)

## 624. feat(user): setup roles table with queries (#3691)

- **Commit:** `e0d8bb20`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-02-19T17:45:42+05:30
- **Changes:** 14 files (+543/-2)

## 625. refactor(merchant_connector_account): change unique constraint to connector label (#3091)

- **Commit:** `073310c1`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-02-20T13:01:30+05:30
- **Changes:** 17 files (+381/-23)

## 626. feat(analytics): added filter api for dispute analytics (#3724)

- **Commit:** `6aeb4409`
- **Author:** harsh-sharma-juspay <125131007+harsh-sharma-juspay@users.noreply.github.com>
- **Date:** 2024-02-20T20:47:02+05:30
- **Changes:** 12 files (+255/-1)

## 627. refactor(permissions): Remove permissions for utility APIs (#3730)

- **Commit:** `4ae28e48`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-02-21T12:50:42+05:30
- **Changes:** 18 files (+179/-118)

## 628. refactor(core): inclusion of locker to store fingerprints (#3630)

- **Commit:** `7b0bce55`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-02-21T13:37:25+05:30
- **Changes:** 20 files (+362/-258)

## 629. refactor(scheduler): improve code reusability and consumer logs (#3712)

- **Commit:** `7c63c760`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-02-21T17:51:59+05:30
- **Changes:** 17 files (+477/-408)

## 630. feat(users): Send email to user if the user already exists (#3705)

- **Commit:** `97252237`
- **Author:** Riddhiagrawal001 <50551695+Riddhiagrawal001@users.noreply.github.com>
- **Date:** 2024-02-21T19:07:49+05:30
- **Changes:** 8 files (+205/-9)

## 631. feat(authz): Add custom role checks in authorization (#3719)

- **Commit:** `ada6a322`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-02-21T19:14:36+05:30
- **Changes:** 15 files (+669/-148)

## 632. feat(user): create apis for custom role  (#3763)

- **Commit:** `58809ab1`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-02-22T19:55:47+05:30
- **Changes:** 17 files (+409/-155)

## 633. feat(payouts): extend routing capabilities to payout operation (#3531)

- **Commit:** `75c633fc`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-02-26T13:00:10+05:30
- **Changes:** 39 files (+1329/-544)

## 634. feat(connector): [Payme] Add Void flow to Payme (#3817)

- **Commit:** `9aabb14a`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-02-26T18:58:03+05:30
- **Changes:** 2 files (+198/-23)

## 635. refactor: incorporate `hyperswitch_interface` into router (#3669)

- **Commit:** `2185cd38`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-26T19:18:18+05:30
- **Changes:** 48 files (+672/-1614)

## 636. feat(connector): mask pii information in connector request and response for stripe, aci, adyen, airwallex  and authorizedotnet (#3678)

- **Commit:** `1c6913be`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-02-27T12:05:41+05:30
- **Changes:** 9 files (+167/-121)

## 637. refactor(payment_methods): introduce `locker_id` column in `payment_methods` table (#3760)

- **Commit:** `38562267`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-02-27T13:33:43+05:30
- **Changes:** 16 files (+398/-237)

## 638. feat(roles): Change list roles, get role and authorization info api to respond with groups (#3837)

- **Commit:** `fbe9d2f1`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-02-27T18:26:46+05:30
- **Changes:** 13 files (+310/-110)

## 639. feat(payouts): Implement Smart Retries for Payout (#3580)

- **Commit:** `8b32dffe`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-02-28T15:08:20+05:30
- **Changes:** 13 files (+685/-83)

## 640. feat(payment_methods): Add default payment method column in customers table and last used column in payment_methods table (#3790)

- **Commit:** `f3931cf4`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-02-28T16:42:58+05:30
- **Changes:** 35 files (+504/-62)

## 641. feat(analytics): adding metric api for dispute analytics (#3810)

- **Commit:** `de6b16be`
- **Author:** harsh-sharma-juspay <125131007+harsh-sharma-juspay@users.noreply.github.com>
- **Date:** 2024-02-28T17:39:31+05:30
- **Changes:** 20 files (+1028/-26)

## 642. refactor(router): add parent caller function for DB (#3838)

- **Commit:** `0936b02a`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-02-29T13:25:49+05:30
- **Changes:** 71 files (+266/-174)

## 643. fix(connector): [adyen] production endpoints and mappings (#3900)

- **Commit:** `8933ddff`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-02-29T23:57:36+05:30
- **Changes:** 17 files (+331/-110)

## 644. chore: adding addition fields from psql to kafka event for analytics usecase (#3815)

- **Commit:** `cc0d0063`
- **Author:** ShivanshMathurJuspay <104988143+ShivanshMathurJuspay@users.noreply.github.com>
- **Date:** 2024-03-01T12:22:41+05:30
- **Changes:** 4 files (+57/-144)

## 645. feat(address): add payment method billing details (#3812)

- **Commit:** `33f07419`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-03-01T17:37:29+05:30
- **Changes:** 90 files (+1683/-208)

## 646. feat(core): diesel models and db interface changes for authentication table (#3859)

- **Commit:** `81626681`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-03-01T18:03:32+05:30
- **Changes:** 10 files (+542/-0)

## 647. feat(webhooks): implement automatic retries for failed webhook deliveries using scheduler (#3842)

- **Commit:** `5bb67c7d`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-03-04T12:01:02+05:30
- **Changes:** 27 files (+964/-214)

## 648. refactor(test_utils): use json to run collection and add run time edit (#3807)

- **Commit:** `a1d63d4b`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2024-03-04T13:11:12+05:30
- **Changes:** 39 files (+231/-369)

## 649. fix(router): [nuvei] Nuvei recurring MIT fix and mandatory details fix (#3602)

- **Commit:** `aa001b45`
- **Author:** cb-alfredjoseph <97145230+cb-alfredjoseph@users.noreply.github.com>
- **Date:** 2024-03-04T20:21:38+05:30
- **Changes:** 2 files (+154/-93)

## 650. fix(router): [nuvei] Nuvei error handling for payment declined status and included tests (#3832)

- **Commit:** `087932f0`
- **Author:** cb-alfredjoseph <97145230+cb-alfredjoseph@users.noreply.github.com>
- **Date:** 2024-03-05T12:10:29+05:30
- **Changes:** 74 files (+3817/-1)

## 651. feat(api_models): add api_models for external 3ds authentication flow (#3858)

- **Commit:** `0a43ceb1`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-03-05T13:19:05+05:30
- **Changes:** 13 files (+601/-8)

## 652. feat(payouts): Implement Single Connector Retry for Payouts (#3908)

- **Commit:** `0cb95a49`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-03-05T13:20:19+05:30
- **Changes:** 3 files (+192/-73)

## 653. feat(roles): Add caching for custom roles (#3946)

- **Commit:** `19c50239`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-03-05T18:56:09+05:30
- **Changes:** 12 files (+191/-31)

## 654. feat(core): external authentication related schema changes for existing tables (#3904)

- **Commit:** `c09b2b3a`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-03-05T19:05:43+05:30
- **Changes:** 27 files (+210/-10)

## 655. ci(postman): hotfix for stripe and nmi collections failing (#3956)

- **Commit:** `1a805679`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2024-03-05T23:52:53+05:30
- **Changes:** 7 files (+3436/-3475)

## 656. feat(core): store customer_acceptance in the payment_methods table (#3885)

- **Commit:** `a1fd36a1`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-03-06T15:00:16+05:30
- **Changes:** 83 files (+574/-126)

## 657. fix(connector): [adyen] handle Webhook reference and object (#3976)

- **Commit:** `0aa40cba`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-03-06T19:58:44+05:30
- **Changes:** 2 files (+238/-54)

## 658. fix(webhooks): abort outgoing webhook retry task if webhook URL is not available in business profile (#3997)

- **Commit:** `ce0ac3d0`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-03-07T18:36:43+05:30
- **Changes:** 2 files (+120/-80)

## 659. feat(router): add domain types, admin core changes and other prerequisites for 3ds external authentication flow (#3962)

- **Commit:** `4902c403`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-03-08T01:26:30+05:30
- **Changes:** 35 files (+509/-27)

## 660. fix(deserialization): deserialize reward payment method data (#4011)

- **Commit:** `f6b44f38`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-03-08T01:52:11+05:30
- **Changes:** 9 files (+468/-4)

## 661. feat(core): add core functions for external authentication (#3969)

- **Commit:** `897e264a`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-03-08T19:16:35+05:30
- **Changes:** 24 files (+766/-5)

## 662. fix(deserialization): error message is different when invalid data is passed for payment method data (#4022)

- **Commit:** `f1fe2954`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-03-09T01:29:50+05:30
- **Changes:** 20 files (+718/-97)

## 663. feat(router): add payments authentication api flow (#3996)

- **Commit:** `41556bae`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-03-09T12:46:09+05:30
- **Changes:** 7 files (+475/-1)

## 664. feat(connector): add threedsecureio three_ds authentication connector (#4004)

- **Commit:** `06c30967`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-03-09T14:48:45+05:30
- **Changes:** 24 files (+1418/-14)

## 665. feat(users): Implemented Set-Cookie (#3865)

- **Commit:** `44eef46e`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-03-11T12:05:18+05:30
- **Changes:** 11 files (+198/-66)

## 666. refactor(core): updated payments response with payment_method_id & payment_method_status (#3883)

- **Commit:** `7391416e`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-03-11T13:04:34+05:30
- **Changes:** 42 files (+277/-65)

## 667. refactor(connector): [adyen] add more fields in the payments request (#4010)

- **Commit:** `5584f113`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-03-11T15:25:59+05:30
- **Changes:** 3 files (+195/-48)

## 668. feat(router): add routing support for token-based mit payments (#4012)

- **Commit:** `43ebfbc4`
- **Author:** Shanks <shashank.attarde@juspay.in>
- **Date:** 2024-03-11T15:26:07+05:30
- **Changes:** 27 files (+429/-180)

## 669. feat(global-search): dashboard globalsearch apis (#3831)

- **Commit:** `ac8ddd40`
- **Author:** ivor-juspay <138492857+ivor-juspay@users.noreply.github.com>
- **Date:** 2024-03-12T13:21:09+05:30
- **Changes:** 16 files (+1135/-351)

## 670. refactor(address): pass payment method billing to the connector module (#3828)

- **Commit:** `195c700e`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-03-12T15:52:52+05:30
- **Changes:** 55 files (+406/-388)

## 671. feat(core): confirm flow and authorization api changes for external authentication (#4015)

- **Commit:** `ce3625cb`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-03-12T16:11:22+05:30
- **Changes:** 19 files (+692/-49)

## 672. feat(webhooks): store request and response payloads in `events` table (#4029)

- **Commit:** `fd67a6c2`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-03-14T12:30:37+05:30
- **Changes:** 32 files (+1270/-647)

## 673. feat(pm_auth): Support different pm types in PM auth (#3114)

- **Commit:** `290c456a`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-03-15T17:57:26+05:30
- **Changes:** 7 files (+256/-74)

## 674. feat(events): Add audit events scaffolding (#3863)

- **Commit:** `6f679851`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2024-03-18T12:11:33+05:30
- **Changes:** 33 files (+302/-294)

## 675. refactor(core): move authentication data fields to authentication table (#4093)

- **Commit:** `a3dec0b6`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-03-19T15:10:18+05:30
- **Changes:** 29 files (+1175/-895)

## 676. feat(payouts): implement KVRouterStore (#3889)

- **Commit:** `944089d6`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-03-19T15:33:37+05:30
- **Changes:** 59 files (+2173/-779)

## 677. feat: store payment check codes and authentication data from processors (#3958)

- **Commit:** `7afc44e8`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-03-20T13:26:20+05:30
- **Changes:** 39 files (+1065/-16)

## 678. refactor(payment_method_data): add a trait to retrieve billing from payment method data (#4095)

- **Commit:** `9b9bce80`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-03-20T16:36:26+05:30
- **Changes:** 1 files (+576/-24)

## 679. feat(payouts): implement list and filter APIs (#3651)

- **Commit:** `fb5f0e6c`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-03-21T14:25:06+05:30
- **Changes:** 26 files (+1615/-25)

## 680. feat(payouts): add payout types in euclid crate (#3862)

- **Commit:** `a1514853`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-03-21T14:26:49+05:30
- **Changes:** 11 files (+278/-19)

## 681. feat(events): add APIs to list webhook events and webhook delivery attempts (#4131)

- **Commit:** `14e1bbaf`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-03-21T19:02:17+05:30
- **Changes:** 54 files (+4218/-2451)

## 682. feat(events): allow listing webhook events and webhook delivery attempts by business profile (#4159)

- **Commit:** `4c8cdf14`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-03-22T17:02:05+05:30
- **Changes:** 9 files (+233/-58)

## 683. fix(log): adding span metadata to `tokio` spawned futures (#4118)

- **Commit:** `07062212`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-03-27T11:46:22+05:30
- **Changes:** 13 files (+117/-86)

## 684. fix(connectors): fix wallet token deserialization error  (#4133)

- **Commit:** `929848f8`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-03-27T11:47:30+05:30
- **Changes:** 22 files (+147/-61)

## 685. feat(connector): [billwerk] add connector template code (#4123)

- **Commit:** `37be05d3`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-03-27T13:37:49+05:30
- **Changes:** 20 files (+1321/-39)

## 686. feat(mandates): allow off-session payments using `payment_method_id` (#4132)

- **Commit:** `7b337ac3`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-03-28T18:12:30+05:30
- **Changes:** 20 files (+429/-173)

## 687. build(deps): bump `error-stack` from version `0.3.1` to `0.4.1` (#4188)

- **Commit:** `ea730d4f`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-04-01T12:31:17+05:30
- **Changes:** 286 files (+1361/-2397)

## 688. feat(connector): [billwerk] implement payment and refund flows (#4245)

- **Commit:** `aecf4aea`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-04-01T19:33:51+05:30
- **Changes:** 20 files (+778/-144)

## 689. refactor(payment_methods): add a new domain type for payment method data to be used in connector module (#4140)

- **Commit:** `9cce1520`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-04-02T13:46:20+05:30
- **Changes:** 120 files (+2232/-1679)

## 690. build(deps): update dependencies (#4268)

- **Commit:** `1f0d60e6`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-04-02T15:43:30+05:30
- **Changes:** 46 files (+1973/-1860)

## 691. feat(analytics): three_ds and authentication events in sdkevents (#4251)

- **Commit:** `88b53b0d`
- **Author:** Vrishab Srivatsa <136090360+vsrivatsa-juspay@users.noreply.github.com>
- **Date:** 2024-04-02T17:39:31+05:30
- **Changes:** 13 files (+914/-29)

## 692. feat(router): [BOA] implement mandates for cards and wallets (#4232)

- **Commit:** `2f304e60`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-04-02T19:43:28+05:30
- **Changes:** 10 files (+986/-299)

## 693. refactor: Fix typos (#4277)

- **Commit:** `36f4112a`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-04-03T13:40:04+05:30
- **Changes:** 285 files (+189/-191)

## 694. feat(api): add browser information in payments response (#3963)

- **Commit:** `4051cbb4`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-04-03T15:16:18+05:30
- **Changes:** 9 files (+252/-308)

## 695. feat(core): update connector_mandate_details in payment_method (#4155)

- **Commit:** `d8028cef`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-04-03T16:52:44+05:30
- **Changes:** 4 files (+214/-49)

## 696. refactor(payment_methods): add Wallets payment method data to new domain type to be used in connector module (#4160)

- **Commit:** `8efd468a`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-03T18:17:43+05:30
- **Changes:** 34 files (+1061/-1000)

## 697. feat(payout-events): add kafka events for payout analytics (#4211)

- **Commit:** `bc25f3fa`
- **Author:** ivor-juspay <138492857+ivor-juspay@users.noreply.github.com>
- **Date:** 2024-04-04T12:54:23+05:30
- **Changes:** 9 files (+251/-3)

## 698. refactor(connector): [Multisafepay] handle authorize and psync 2xx failure error response (#4124)

- **Commit:** `9ebe0f43`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-04-04T13:03:49+05:30
- **Changes:** 3 files (+165/-63)

## 699. feat(webhooks): allow manually retrying delivery of outgoing webhooks (#4176)

- **Commit:** `63d2b685`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-04-04T14:37:51+05:30
- **Changes:** 16 files (+449/-64)

## 700. feat(router): Use `NTID` in `MIT` payments if the `pg_agnostic_mit` config is enabled (#4113)

- **Commit:** `b58d7a8e`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-04-04T18:19:33+05:30
- **Changes:** 4 files (+223/-58)

## 701. fix(payouts): persist status updates in payouts table (#4280)

- **Commit:** `02ffe7e4`
- **Author:** Kashif <46213975+kashif-m@users.noreply.github.com>
- **Date:** 2024-04-04T19:13:24+05:30
- **Changes:** 11 files (+232/-61)

## 702. fix(locker): handle card duplication in payouts flow (#4013)

- **Commit:** `2fac4366`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-04-05T12:19:36+05:30
- **Changes:** 3 files (+281/-107)

## 703. refactor(payment_methods): add PayLater payment method data to new domain type to be used in connector module (#4165)

- **Commit:** `66948527`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-05T18:05:18+05:30
- **Changes:** 11 files (+231/-207)

## 704. feat(connector): [Ebanx] Template for ebanx payout (#4141)

- **Commit:** `ed186a5a`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-04-08T12:34:09+05:30
- **Changes:** 18 files (+1289/-9)

## 705. refactor(payment_methods): add BankRedirect payment method data to new domain type to be used in connector module (#4175)

- **Commit:** `e0e84371`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-08T17:50:05+05:30
- **Changes:** 19 files (+896/-807)

## 706. refactor(card): use `billing.first_name` instead of `card_holder_name` (#4239)

- **Commit:** `8b66cdaa`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-04-10T12:55:14+05:30
- **Changes:** 38 files (+301/-136)

## 707. feat(payouts): add kafka events (#4264)

- **Commit:** `a2958c33`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-04-10T14:43:20+05:30
- **Changes:** 16 files (+241/-102)

## 708. refactor(payment_methods): add some payment method data to new domain type to be used in connector module (#4234)

- **Commit:** `ce1e165c`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-10T14:52:19+05:30
- **Changes:** 11 files (+337/-159)

## 709. feat(events): Add events framework for registering events (#4115)

- **Commit:** `3963219e`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2024-04-10T18:08:40+05:30
- **Changes:** 53 files (+756/-291)

## 710. feat(connector): [ZSL] add connector template code  (#4285)

- **Commit:** `086516b7`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-04-10T18:55:33+05:30
- **Changes:** 22 files (+589/-34)

## 711. feat(payment_methods): added kv support for payment_methods table (#4311)

- **Commit:** `eb3cecdd`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2024-04-10T19:29:50+05:30
- **Changes:** 35 files (+1016/-314)

## 712. refactor(payment_methods): add BankDebit payment method data to new domain type to be used in connector module (#4238)

- **Commit:** `2bf775a9`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-10T20:01:24+05:30
- **Changes:** 14 files (+297/-367)

## 713. refactor(connectors): [ZSL] add Local bank Transfer (#4337)

- **Commit:** `266a075a`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-04-11T22:43:39+05:30
- **Changes:** 51 files (+2868/-178)

## 714. feat(customer): Customer kv impl (#4267)

- **Commit:** `c980f016`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2024-04-12T12:41:03+05:30
- **Changes:** 22 files (+730/-156)

## 715. feat(core): create mandates with payment_token (#4342)

- **Commit:** `53697fb4`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-04-12T15:43:01+05:30
- **Changes:** 17 files (+314/-211)

## 716. refactor(payment_methods): add BankTransfer payment method data to new domain type to be used in connector module (#4260)

- **Commit:** `08d08114`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-12T15:54:05+05:30
- **Changes:** 8 files (+341/-178)

## 717. fix: revert payment method kv changes (#4351)

- **Commit:** `bb202e39`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2024-04-12T17:37:03+05:30
- **Changes:** 1 files (+322/-323)

## 718. feat(events): Add payment cancel events (#4166)

- **Commit:** `dea21c65`
- **Author:** Sampras Lopes <lsampras@pm.me>
- **Date:** 2024-04-15T16:05:40+05:30
- **Changes:** 34 files (+269/-91)

## 719. feat(mandate_kv): add kv support for mandate (#4275)

- **Commit:** `00340a33`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2024-04-16T15:35:15+05:30
- **Changes:** 17 files (+626/-122)

## 720. feat(connector): integrate netcetera connector with pre authentication flow (#4293)

- **Commit:** `d4dbaadb`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-04-16T15:54:06+05:30
- **Changes:** 31 files (+1074/-16)

## 721. feat(router): add external authentication webhooks flow (#4339)

- **Commit:** `00cd96d0`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-04-16T15:54:46+05:30
- **Changes:** 22 files (+511/-94)

## 722. fix: added find all support for pm kv (#4357)

- **Commit:** `5b811aac`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2024-04-16T16:16:37+05:30
- **Changes:** 4 files (+437/-322)

## 723. refactor(payment_methods): revamp payment methods update endpoint (#4305)

- **Commit:** `3333bbfe`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-04-16T22:08:47+05:30
- **Changes:** 11 files (+418/-113)

## 724. feat(router): add retrieve poll status api (#4358)

- **Commit:** `ca47ea9b`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-04-17T15:50:53+05:30
- **Changes:** 21 files (+254/-6)

## 725. feat(payment_methods): Client secret implementation in payment method… (#4134)

- **Commit:** `43307815`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-04-19T17:32:06+05:30
- **Changes:** 27 files (+548/-60)

## 726. feat(router): add poll ability in external 3ds authorization flow (#4393)

- **Commit:** `44765538`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-04-22T21:06:47+05:30
- **Changes:** 11 files (+358/-88)

## 727. feat(connector): implement authentication flow for netcetera (#4334)

- **Commit:** `5ce0535b`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-04-23T15:47:53+05:30
- **Changes:** 10 files (+2092/-37)

## 728. refactor(voucher): remove billing details from voucher pmd (#4361)

- **Commit:** `2dd0ee68`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-04-25T11:39:06+05:30
- **Changes:** 5 files (+140/-140)

## 729. feat(core): [Payouts] Add access_token flow for Payout Create and Fulfill flow (#4375)

- **Commit:** `7f0d04fe`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-04-25T12:02:42+05:30
- **Changes:** 6 files (+420/-87)

## 730. Refactor(core): make save_payment_method as post_update_tracker trait function (#4307)

- **Commit:** `5f40eee3`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-04-25T13:31:43+05:30
- **Changes:** 20 files (+546/-657)

## 731. feat: add an api for toggling extended card info feature (#4444)

- **Commit:** `87d9fced`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-04-25T18:10:00+05:30
- **Changes:** 16 files (+184/-19)

## 732. refactor(required_fields): change required fields for billing address (#4258)

- **Commit:** `e730030e`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-04-26T11:43:10+05:30
- **Changes:** 1 files (+427/-355)

## 733. feat(FRM): Revise post FRM core flows (#4394)

- **Commit:** `01ec7c64`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-04-29T12:27:12+05:30
- **Changes:** 20 files (+337/-125)

## 734. feat: stripe connect integration for payouts (#2041)

- **Commit:** `ac9d856a`
- **Author:** Kashif <mohammed.kashif@juspay.in>
- **Date:** 2024-04-29T15:29:32+05:30
- **Changes:** 40 files (+1778/-268)

## 735. refactor(user): Deprecate Signin, Verify email and Invite v1 APIs (#4465)

- **Commit:** `b0133f33`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-04-30T15:28:45+05:30
- **Changes:** 7 files (+3/-351)

## 736. feat(connector): [Ebanx] Add payout flows  (#4146)

- **Commit:** `4f4cbdff`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-05-02T12:44:35+05:30
- **Changes:** 19 files (+749/-508)

## 737. feat(connector): [Paypal] Add payout flow for wallet(Paypal and Venmo) (#4406)

- **Commit:** `e4ed1e63`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-05-02T15:45:17+05:30
- **Changes:** 20 files (+421/-8)

## 738. feat(opensearch): refactoring (#4244)

- **Commit:** `22cb01ac`
- **Author:** ivor-juspay <138492857+ivor-juspay@users.noreply.github.com>
- **Date:** 2024-05-02T15:50:58+05:30
- **Changes:** 16 files (+691/-149)

## 739. feat: store encrypted extended card info in redis (#4493)

- **Commit:** `6c59d243`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-05-02T16:58:44+05:30
- **Changes:** 8 files (+268/-3)

## 740. feat(core): Rename crate data_models to hyperswitch_domain_models (#4504)

- **Commit:** `86e93cd3`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-05-02T17:56:11+05:30
- **Changes:** 77 files (+309/-258)

## 741. Refactor(Connectors): [BOA] enhance response objects (#4508)

- **Commit:** `3ed0e8b7`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-05-02T20:13:08+05:30
- **Changes:** 1 files (+384/-25)

## 742. feat(users): Create Decision manager for User Flows (#4518)

- **Commit:** `4b3faf67`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-05-02T20:28:44+05:30
- **Changes:** 10 files (+393/-18)

## 743. fix(api_request): make `payment_method_data` as optional (#4527)

- **Commit:** `83a19246`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-05-03T13:50:17+05:30
- **Changes:** 12 files (+160/-70)

## 744. feat(constraint_graph): make the constraint graph framework generic and move it into a separate crate (#3071)

- **Commit:** `a23a365c`
- **Author:** Shanks <shashank.attarde@juspay.in>
- **Date:** 2024-05-06T18:38:44+05:30
- **Changes:** 25 files (+2048/-1138)

## 745. feat(connector): [Cybersource] Add payout flows for Card (#4511)

- **Commit:** `a72f040d`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-05-07T12:48:22+05:30
- **Changes:** 7 files (+434/-10)

## 746. refactor(core): refactor authentication core to fetch authentication only within it (#4138)

- **Commit:** `71a070e2`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-05-07T13:38:53+05:30
- **Changes:** 8 files (+336/-395)

## 747. feat(users): Create Token only support for pre-login user flow APIs (#4558)

- **Commit:** `5ec00d96`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-05-07T14:57:05+05:30
- **Changes:** 8 files (+343/-41)

## 748. refactor: remove `configs/pg_agnostic_mit` api as it will not be used (#4486)

- **Commit:** `99bbc398`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-05-07T15:21:20+05:30
- **Changes:** 12 files (+29/-188)

## 749. chore: address Rust 1.78 clippy lints (#4545)

- **Commit:** `2216a88d`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-05-07T16:05:32+05:30
- **Changes:** 222 files (+1138/-1631)

## 750. feat(connector): [MiFinity] add connector template code (#4447)

- **Commit:** `d974e6e7`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-07T19:20:43+05:30
- **Changes:** 23 files (+1296/-12)

## 751. feat(users): implement force set and force change password (#4564)

- **Commit:** `59e79ff2`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-05-07T19:41:24+05:30
- **Changes:** 25 files (+240/-34)

## 752. refactor(bank-debit): remove billingdetails from bankdebit pmd (#4371)

- **Commit:** `625b5318`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-08T11:45:47+05:30
- **Changes:** 12 files (+142/-289)

## 753. feat(users): Create `user_key_store` table and `begin_totp` API (#4577)

- **Commit:** `a97016fe`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-05-08T18:25:45+05:30
- **Changes:** 30 files (+649/-27)

## 754. feat(connector): [Payone] add connector template code (#4469)

- **Commit:** `f386f423`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-05-09T15:31:47+05:30
- **Changes:** 23 files (+1286/-11)

## 755. fix(connector): [BAMBORA] Audit Fixes for Bambora (#4604)

- **Commit:** `366596f1`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-05-09T18:36:38+05:30
- **Changes:** 5 files (+516/-413)

## 756. feat(users): new routes to accept invite and list merchants (#4591)

- **Commit:** `e70d58af`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-05-09T18:39:13+05:30
- **Changes:** 10 files (+216/-25)

## 757. refactor(billing): store `payment_method_data_billing` for recurring payments (#4513)

- **Commit:** `55ae0fc5`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-05-09T18:42:05+05:30
- **Changes:** 18 files (+333/-152)

## 758. feat(Connectors): add mandate validation for auth flow (#4089)

- **Commit:** `fef28c33`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-05-10T15:01:44+05:30
- **Changes:** 20 files (+582/-38)

## 759. feat(analytics): authentication analytics (#4429)

- **Commit:** `24d15424`
- **Author:** Vrishab Srivatsa <136090360+vsrivatsa-juspay@users.noreply.github.com>
- **Date:** 2024-05-10T15:38:26+05:30
- **Changes:** 28 files (+790/-418)

## 760. refactor(bank-transfer): remove billing from banktransfer payment data (#4377)

- **Commit:** `0f5a370b`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-13T11:50:08+05:30
- **Changes:** 7 files (+303/-407)

## 761. refactor(card_details): added missing card data fields for connectors (#4571)

- **Commit:** `41655ba3`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-05-13T12:22:26+05:30
- **Changes:** 1 files (+1671/-527)

## 762. feat(connector): generate connector template code for gpayments authenticaition connector (#4584)

- **Commit:** `2a302eb5`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-05-13T14:51:14+05:30
- **Changes:** 21 files (+401/-12)

## 763. feat(refunds): update refunds filters (#4409)

- **Commit:** `cfab2af7`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-05-13T18:47:29+05:30
- **Changes:** 14 files (+254/-12)

## 764. feat(payment_methods): pass `required_billing_contact_fields` field in `/session` call based on dynamic fields (#4601)

- **Commit:** `348cd744`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-05-13T19:32:00+05:30
- **Changes:** 10 files (+246/-6)

## 765. refactor(connector): [BOA/CYBS] refund error handling (#4632)

- **Commit:** `99702ed8`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-05-14T12:37:40+05:30
- **Changes:** 4 files (+170/-74)

## 766. refactor: remove `Ctx` generic from payments core (#4574)

- **Commit:** `6b509c7b`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-05-14T18:18:18+05:30
- **Changes:** 32 files (+505/-746)

## 767. feat(payment_methods): pass required shipping details field for wallets session call based on `business_profile` config (#4616)

- **Commit:** `650f3fa2`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-05-14T20:25:52+05:30
- **Changes:** 30 files (+692/-30)

## 768. feat(core): Move RouterData to crate hyperswitch_domain_models (#4524)

- **Commit:** `ff1c2ddf`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-05-15T12:23:50+05:30
- **Changes:** 48 files (+584/-477)

## 769. refactor(bank-redirect): remove billing from bankredirect payment data (#4362)

- **Commit:** `0958d948`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-15T13:24:28+05:30
- **Changes:** 14 files (+213/-429)

## 770. feat(middleware): log content_length for 4xx (#4655)

- **Commit:** `4b5b558d`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-05-16T16:00:50+05:30
- **Changes:** 19 files (+164/-195)

## 771. refactor(FRM): refactor frm configs (#4581)

- **Commit:** `853f3b48`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-05-17T15:53:13+05:30
- **Changes:** 32 files (+137/-148)

## 772. feat: Soft kill kv (#4582)

- **Commit:** `3fa59d4b`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2024-05-20T12:47:05+05:30
- **Changes:** 32 files (+462/-118)

## 773. feat(core): Add a new endpoint for Complete Authorize flow (#4686)

- **Commit:** `226c3373`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-20T21:32:36+05:30
- **Changes:** 14 files (+267/-21)

## 774. refactor(router): added a new type minor unit to amount (#4629)

- **Commit:** `443b7e6e`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-05-21T15:40:05+05:30
- **Changes:** 61 files (+679/-436)

## 775. feat(constraint_graph): add visualization functionality to the constraint graph (#4701)

- **Commit:** `0f53f74d`
- **Author:** Shanks <shashank.attarde@juspay.in>
- **Date:** 2024-05-21T17:28:52+05:30
- **Changes:** 9 files (+197/-3)

## 776. refactor(graph): refactor the Knowledge Graph to include configs check, while eligibility analysis (#4687)

- **Commit:** `a917776b`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-05-21T19:44:45+05:30
- **Changes:** 19 files (+542/-35)

## 777. feat(webhook): add frm webhook support (#4662)

- **Commit:** `ae601e8e`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-05-22T13:45:01+05:30
- **Changes:** 7 files (+400/-38)

## 778. feat(routing): Use Moka cache for routing with cache invalidation (#3216)

- **Commit:** `431560b7`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-05-22T14:02:50+05:30
- **Changes:** 9 files (+134/-122)

## 779. feat(connector): [AUTHORIZEDOTNET] Implement zero mandates (#4704)

- **Commit:** `8afeda54`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-05-22T17:21:06+05:30
- **Changes:** 2 files (+421/-128)

## 780. refactor(bank-redirect): dynamic field changes for bankredirect payment method (#4650)

- **Commit:** `da2dc10f`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-23T12:23:25+05:30
- **Changes:** 1 files (+164/-72)

## 781. chore: move RouterData Request types to hyperswitch_domain_models crate (#4723)

- **Commit:** `ae77373b`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-05-23T15:48:51+05:30
- **Changes:** 38 files (+2397/-1943)

## 782. feat(payment_charges): add support for collecting and refunding charges on payments (#4628)

- **Commit:** `55ccce61`
- **Author:** Kashif <mohammed.kashif@juspay.in>
- **Date:** 2024-05-24T13:39:04+05:30
- **Changes:** 106 files (+882/-22)

## 783. Refactor(core): Inclusion of constraint graph for merchant Payment Method list (#4626)

- **Commit:** `2cabb0be`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-05-24T17:35:21+05:30
- **Changes:** 7 files (+1084/-458)

## 784. feat(core): [Paypal] Add session_token flow for Paypal sdk (#4697)

- **Commit:** `b3d4d13d`
- **Author:** SamraatBansal <55536657+SamraatBansal@users.noreply.github.com>
- **Date:** 2024-05-27T16:35:07+05:30
- **Changes:** 28 files (+526/-102)

## 785. feat(connector): [AUTHORIZEDOTNET] Implement non-zero mandates (#4758)

- **Commit:** `ed82af81`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-05-27T22:27:07+05:30
- **Changes:** 2 files (+317/-115)

## 786. feat(connector): [Iatapay] add upi qr support (#4728)

- **Commit:** `c9fa94fe`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-05-28T13:06:53+05:30
- **Changes:** 22 files (+257/-65)

## 787. refactor(core): move router data response and request models to hyperswitch domain models crate (#4789)

- **Commit:** `dd333298`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-05-29T13:29:33+05:30
- **Changes:** 21 files (+543/-859)

## 788. refactor(connector): [Klarna] Refactor Authorize call and configs for prod (#4750)

- **Commit:** `a6570b6a`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-29T15:39:10+05:30
- **Changes:** 17 files (+199/-61)

## 789. feat(users): Add redis in Begin and Verify TOTP and create a new API that updates TOTP (#4765)

- **Commit:** `cd9c9b60`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-05-29T15:39:28+05:30
- **Changes:** 10 files (+205/-96)

## 790. feat(connector): [Klarna] Add support for Capture, Psync, Refunds and Rsync flows (#4799)

- **Commit:** `e41d5e25`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-05-29T20:29:56+05:30
- **Changes:** 3 files (+643/-41)

## 791. chore: remove redundant caching code (#4804)

- **Commit:** `971ef1fb`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-05-30T13:06:52+05:30
- **Changes:** 17 files (+149/-283)

## 792. feat(connector): implement pre auth flow for gpayments (#4692)

- **Commit:** `bed42ce4`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-05-30T13:13:22+05:30
- **Changes:** 18 files (+632/-67)

## 793. feat(payout): [Payone] add payone connector (#4553)

- **Commit:** `832968c0`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-05-30T15:12:02+05:30
- **Changes:** 14 files (+444/-509)

## 794. feat: add a domain type for `customer_id` (#4705)

- **Commit:** `93d61d10`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-05-30T16:19:10+05:30
- **Changes:** 106 files (+1150/-490)

## 795. feat(router): Added amount conversion function in core for connector module (#4710)

- **Commit:** `08eefdba`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-05-30T19:21:33+05:30
- **Changes:** 30 files (+577/-150)

## 796. refactor(core): move router data flow types to hyperswitch domain models crate (#4801)

- **Commit:** `61e67e42`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-05-30T20:24:50+05:30
- **Changes:** 18 files (+148/-116)

## 797. Refactor(core): Reverts Inclusion of constraint graph for merchant Payment Method list (#4839)

- **Commit:** `f74b9b62`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-05-31T18:31:50+05:30
- **Changes:** 7 files (+458/-1084)

## 798. feat(consolidated-kafka-events): add consolidated kafka payment events (#4798)

- **Commit:** `ccee1a9c`
- **Author:** ivor-juspay <138492857+ivor-juspay@users.noreply.github.com>
- **Date:** 2024-06-03T14:46:17+05:30
- **Changes:** 10 files (+455/-39)

## 799. refactor(connector): airwallex convert init payment to preprocessing (#4842)

- **Commit:** `e5da133f`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-03T16:21:49+05:30
- **Changes:** 22 files (+851/-55)

## 800. feat(multitenancy): add support for multitenancy and handle the same in router, producer, consumer, drainer and analytics (#4630)

- **Commit:** `15d6c3e8`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2024-06-03T17:57:30+05:30
- **Changes:** 188 files (+2261/-1415)

## 801. refactor(connector): move AuthorizeSessionToken flow to core from execute_pretasks for nuvei and square (#4854)

- **Commit:** `32f0fae2`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-05T13:39:29+05:30
- **Changes:** 7 files (+157/-74)

## 802. feat(core): Create Payout Webhook Flow (#4696)

- **Commit:** `a3183a0c`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-06-05T14:58:42+05:30
- **Changes:** 43 files (+809/-68)

## 803. chore(users): email templates updated (#4562)

- **Commit:** `7ab65ac8`
- **Author:** Gitanjli <96485413+gitanjli525@users.noreply.github.com>
- **Date:** 2024-06-05T16:41:36+05:30
- **Changes:** 8 files (+1358/-1527)

## 804. feat(connector): add payouts integration for AdyenPlatform (#4874)

- **Commit:** `32cf06c7`
- **Author:** Kashif <mohammed.kashif@juspay.in>
- **Date:** 2024-06-05T17:12:50+05:30
- **Changes:** 47 files (+896/-51)

## 805. feat(multitenancy): move users and tenants to global schema (#4781)

- **Commit:** `c5e28f26`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2024-06-05T18:50:40+05:30
- **Changes:** 16 files (+278/-86)

## 806. Refactor(core): Inclusion of constraint graph for merchant Payment Method list (#4845)

- **Commit:** `4df84e91`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-06-05T20:42:22+05:30
- **Changes:** 7 files (+986/-458)

## 807. refactor(connector): [BOA/CYBS] add customer token for mandates and refactor psync  (#4815)

- **Commit:** `3d53fd01`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-06-05T23:45:01+05:30
- **Changes:** 7 files (+649/-331)

## 808. feat(router): add an api to migrate the apple pay certificates from connector metadata to `connector_wallets_details` column in merchant connector account (#4790)

- **Commit:** `7a942375`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-06-06T13:53:03+05:30
- **Changes:** 52 files (+763/-173)

## 809. refactor(webhooks): extract incoming and outgoing webhooks into separate modules (#4870)

- **Commit:** `b1cb053a`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-06-06T14:00:09+05:30
- **Changes:** 5 files (+2412/-2380)

## 810. feat(connector): [MIFINITY] Implement payment flows and Mifinity payment method (#4592)

- **Commit:** `6750be5a`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-06-06T17:47:45+05:30
- **Changes:** 58 files (+758/-375)

## 811. refactor(connector): convert init payment flow to preprocessing flow for nuvei (#4878)

- **Commit:** `e7acaa57`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-06T18:51:09+05:30
- **Changes:** 9 files (+233/-100)

## 812. refactor(outgoing_webhooks): raise errors in the analytics pipeline in case of API client errors or non-2xx responses (#4894)

- **Commit:** `9da92027`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-06-06T23:15:45+05:30
- **Changes:** 1 files (+258/-223)

## 813. refactor(openapi): move openapi to a separate folder (#4859)

- **Commit:** `05105321`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-06-07T11:44:01+05:30
- **Changes:** 110 files (+1217/-4628)

## 814. refactor(connector): convert init payment flow to preprocessing flow for shift4 (#4884)

- **Commit:** `5b92371a`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-07T12:34:07+05:30
- **Changes:** 8 files (+146/-103)

## 815. refactor(payout): move payout quote call to payout core from execute_pretasks (#4900)

- **Commit:** `d0fd7095`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-07T16:14:05+05:30
- **Changes:** 10 files (+71/-160)

## 816. ci(postman): add users collection (#4897)

- **Commit:** `a2b17cbc`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-06-10T18:17:53+05:30
- **Changes:** 42 files (+1181/-10)

## 817. refactor(conditional_configs): refactor conditional_configs to use Moka Cache instead of Static Cache (#4814)

- **Commit:** `4d0c8936`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-06-11T13:17:25+05:30
- **Changes:** 13 files (+179/-170)

## 818. refactor(connector): changed amount to minor Unit for stripe (#4786)

- **Commit:** `b705757b`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-06-11T13:27:24+05:30
- **Changes:** 27 files (+184/-58)

## 819. feat(connector): [Multisafepay] Add support for Ideal and Giropay  (#4398)

- **Commit:** `b01bbba6`
- **Author:** Taksh Panchal <takshtax@gmail.com>
- **Date:** 2024-06-11T19:15:03+05:30
- **Changes:** 5 files (+293/-12)

## 820. feat(connector): implement auth and post auth flows for gpayments (#4746)

- **Commit:** `d93f65fd`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-06-12T00:05:31+05:30
- **Changes:** 3 files (+459/-23)

## 821. feat(connector): [BOA/CYB] Make billTo fields optional (#4951)

- **Commit:** `4651584e`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-06-12T17:37:55+05:30
- **Changes:** 2 files (+166/-102)

## 822. feat(connectors): [Iatapay] add payment methods (#4968)

- **Commit:** `0e059e7d`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-06-13T09:15:09+05:30
- **Changes:** 74 files (+588/-43)

## 823. feat(router): include the pre-routing connectors in Apple Pay retries (#4952)

- **Commit:** `fb836618`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-06-13T16:41:43+05:30
- **Changes:** 5 files (+201/-104)

## 824. feat(connector): added template code for datatrans (#4890)

- **Commit:** `65827290`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-06-14T15:29:31+05:30
- **Changes:** 22 files (+1283/-7)

## 825. refactor: Move trait ConnectorIntegration to crate hyperswitch_interfaces (#4946)

- **Commit:** `cbe3a6d4`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-06-18T13:53:40+05:30
- **Changes:** 19 files (+635/-509)

## 826. refactor: add basic counter metrics for IMC (#5006)

- **Commit:** `d2092dcb`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-06-18T18:29:12+05:30
- **Changes:** 43 files (+301/-316)

## 827. refactor(connector): add amount conversion framework for noon (#4843)

- **Commit:** `8c7e1a3b`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-06-19T16:06:33+05:30
- **Changes:** 7 files (+142/-76)

## 828. refactor(storage): remove `id` from payment intent, attempt and remove datamodel ext from payment intent (#4923)

- **Commit:** `bec51a35`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-06-19T17:10:32+05:30
- **Changes:** 71 files (+1319/-935)

## 829. Refactor(core): reverts the payment method list filtering using constraint graph (#5044)

- **Commit:** `e486641c`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-06-19T20:25:29+05:30
- **Changes:** 8 files (+462/-264)

## 830. refactor: introduce ConnectorIntegrationNew and add default implementation for each Connector (#4989)

- **Commit:** `84bed81d`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-20T15:54:48+05:30
- **Changes:** 28 files (+3456/-86)

## 831. feat(payment_methods): Implement Process tracker workflow for Payment method Status update (#4668)

- **Commit:** `5cde7ee0`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-06-21T14:21:14+05:30
- **Changes:** 8 files (+211/-4)

## 832. feat(users): setup user authentication methods schema and apis (#4999)

- **Commit:** `2005d3df`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-06-21T16:29:17+05:30
- **Changes:** 29 files (+888/-16)

## 833. refactor(redis): spawn one subscriber thread for handling all the published messages to different channel (#5064)

- **Commit:** `6a07e10a`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-06-21T17:01:52+05:30
- **Changes:** 5 files (+160/-126)

## 834. refactor(events): populate object identifiers in outgoing webhooks analytics events during retries (#5067)

- **Commit:** `b8784059`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-06-24T12:56:19+05:30
- **Changes:** 13 files (+177/-104)

## 835. refactor(core): introduce an interface to switch between old and new connector integration implementations on the connectors (#5013)

- **Commit:** `e658899c`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-06-24T15:10:34+05:30
- **Changes:** 103 files (+2153/-683)

## 836. feat: added kafka events for authentication create and update (#4991)

- **Commit:** `10e91213`
- **Author:** Vrishab Srivatsa <136090360+vsrivatsa-juspay@users.noreply.github.com>
- **Date:** 2024-06-24T18:10:50+05:30
- **Changes:** 10 files (+491/-26)

## 837. refactor: separate DB queries and HTML creation for payout links (#4967)

- **Commit:** `9e4b2d1c`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-06-25T19:37:10+05:30
- **Changes:** 92 files (+4442/-199)

## 838. refactor(connector): add amount framework to payme & Trustpay with googlePay, ApplePay for bluesnap, Noon & Trustpay (#4833)

- **Commit:** `e69a7bda`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-06-26T14:44:48+05:30
- **Changes:** 14 files (+224/-146)

## 839. feat: realtime user analytics (#5098)

- **Commit:** `cd5a1a34`
- **Author:** Vrishab Srivatsa <136090360+vsrivatsa-juspay@users.noreply.github.com>
- **Date:** 2024-06-26T17:23:39+05:30
- **Changes:** 32 files (+826/-26)

## 840. fix(docs): open-api fix for payment response (#5103)

- **Commit:** `2e1167ac`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-06-26T19:00:02+05:30
- **Changes:** 3 files (+299/-8)

## 841. feat(router): add payments manual-update api (#5045)

- **Commit:** `ed021c1d`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-06-26T19:10:09+05:30
- **Changes:** 13 files (+292/-8)

## 842. feat(users): implemented openidconnect (#5124)

- **Commit:** `ce7d0d42`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-06-26T19:15:55+05:30
- **Changes:** 22 files (+877/-41)

## 843. fix(opensearch): show search results only if user has access permission to the index  (#5097)

- **Commit:** `9c49ded1`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-06-27T13:06:31+05:30
- **Changes:** 7 files (+130/-78)

## 844. feat(router): skip apple pay session call if the browser is not Safari (#5136)

- **Commit:** `d4dba55f`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-06-27T18:08:07+05:30
- **Changes:** 26 files (+216/-65)

## 845. chore: use generic phone numbers instead (#5142)

- **Commit:** `57055eca`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2024-06-27T23:35:56+05:30
- **Changes:** 144 files (+420/-420)

## 846. refactor(connector): added amount framework to paypal, payouts and routing (#4865)

- **Commit:** `b08ce221`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-06-28T12:01:15+05:30
- **Changes:** 34 files (+204/-181)

## 847. feat(core): customer_details storage in payment_intent (#5007)

- **Commit:** `bb9a9715`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-06-28T15:06:19+05:30
- **Changes:** 20 files (+380/-110)

## 848. Docs: Api reference docs update for Payments - Create (#4955)

- **Commit:** `f55cae20`
- **Author:** GORAKHNATH YADAV <gorakhcodes@gmail.com>
- **Date:** 2024-06-28T17:02:38+05:30
- **Changes:** 9 files (+743/-228)

## 849. feat(connector): [Bambora Apac] Template for integration (#5062)

- **Commit:** `1b894632`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-01T16:28:36+05:30
- **Changes:** 21 files (+1300/-10)

## 850. feat(payment_link): add multiple custom css support in business level  (#5137)

- **Commit:** `ecc6c00d`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-07-01T16:29:06+05:30
- **Changes:** 10 files (+165/-96)

## 851. feat(analytics): Add v2 payment analytics (payment-intents analytics) (#5150)

- **Commit:** `9fc525d4`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-07-01T17:45:46+05:30
- **Changes:** 23 files (+1641/-89)

## 852. fix(router): mark retry payment as failure if `connector_tokenization` fails (#5114)

- **Commit:** `ecb8cafa`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-07-01T20:07:41+05:30
- **Changes:** 9 files (+146/-70)

## 853. refactor: use hashmap deserializer for generic_link options (#5157)

- **Commit:** `a343f69d`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-07-02T15:16:20+05:30
- **Changes:** 23 files (+310/-90)

## 854. fix(router): [CYBS] make payment status optional (#5165)

- **Commit:** `e3470a24`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-07-02T17:12:18+05:30
- **Changes:** 2 files (+154/-217)

## 855. feat(analytics): FRM Analytics (#4880)

- **Commit:** `cc88c070`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-07-04T12:22:27+05:30
- **Changes:** 36 files (+1629/-78)

## 856. feat(core): Added integrity framework for Authorize and Sync flow with connector as Stripe (#5109)

- **Commit:** `c8c0cb76`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-07-04T15:06:06+05:30
- **Changes:** 37 files (+721/-230)

## 857. Docs: Updated API - ref for payments (#5172)

- **Commit:** `cf5c1041`
- **Author:** GORAKHNATH YADAV <gorakhcodes@gmail.com>
- **Date:** 2024-07-04T18:43:54+05:30
- **Changes:** 4 files (+140/-118)

## 858. Feat(connector): [BRAINTREE] Implement Card Mandates (#5204)

- **Commit:** `1904ffad`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-07-05T13:37:46+05:30
- **Changes:** 13 files (+246/-49)

## 859. feat(core): billing_details inclusion in Payment Intent (#5090)

- **Commit:** `ec01788b`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-07-05T18:43:46+05:30
- **Changes:** 42 files (+212/-144)

## 860. fix(analytics): using HashSet to represent the returned metrics (#5179)

- **Commit:** `16e8f4b2`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-07-05T18:48:51+05:30
- **Changes:** 52 files (+214/-114)

## 861. feat(events): Add payment metadata to hyperswitch-payment-intent-events (#5170)

- **Commit:** `5ebfbaf1`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-07-05T20:15:25+05:30
- **Changes:** 25 files (+146/-119)

## 862. refactor: fix unit and documentation tests (#4754)

- **Commit:** `648cecb2`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-07-05T23:37:39+05:30
- **Changes:** 17 files (+178/-154)

## 863. feat(core): addition of shipping address details in payment intent (#5112)

- **Commit:** `2d31d38c`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-07-08T15:13:19+05:30
- **Changes:** 16 files (+243/-241)

## 864. feat(router): add integrity check for refund refund sync and capture flow with stripe as connector (#5187)

- **Commit:** `adc760f0`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-07-08T20:39:58+05:30
- **Changes:** 17 files (+427/-44)

## 865. feat: add `hsdev` binary to run migrations (#4877)

- **Commit:** `f64b5221`
- **Author:** David Kurilla <130074511+davidkurilla@users.noreply.github.com>
- **Date:** 2024-07-08T10:12:25-07:00
- **Changes:** 5 files (+342/-8)

## 866. feat(decision): add support to register api keys to proxy (#5168)

- **Commit:** `071d5345`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2024-07-09T13:05:20+05:30
- **Changes:** 7 files (+329/-2)

## 867. feat(connector): [RazorPay] Add new connector and Implement payment flows for UPI payment method (#5200)

- **Commit:** `fdac3132`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-07-09T20:04:20+05:30
- **Changes:** 30 files (+2644/-6)

## 868. feat(core): Constraint Graph for Payment Methods List (#5081)

- **Commit:** `82c6e0e6`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-07-09T22:45:15+05:30
- **Changes:** 17 files (+1286/-539)

## 869. feat(merchant_account): add merchant account create v2 route (#5061)

- **Commit:** `d6b9151e`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-07-10T13:15:36+05:30
- **Changes:** 36 files (+1553/-957)

## 870. feat(connector): [Bambora APAC] Add payment flows (#5193)

- **Commit:** `f7abcee6`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-10T16:24:31+05:30
- **Changes:** 17 files (+1073/-233)

## 871. feat(router): add an api to migrate the payment method (#5186)

- **Commit:** `125699f8`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-07-10T22:01:13+05:30
- **Changes:** 16 files (+696/-31)

## 872. fix(payments_create): save the `customer_id` in payments create (#5262)

- **Commit:** `53cb9537`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-07-10T22:09:36+05:30
- **Changes:** 6 files (+180/-102)

## 873. refactor: Move trait IncomingWebhook to hyperswitch_interfaces (#5191)

- **Commit:** `35d502e3`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-07-11T16:01:31+05:30
- **Changes:** 27 files (+612/-573)

## 874. fix(connector): [BANKOFAMERICA] Remove cards 3ds flow (#5294)

- **Commit:** `7c408aff`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-07-11T18:04:25+05:30
- **Changes:** 4 files (+31/-1099)

## 875. feat: create key in encryption service for merchant and user (#4910)

- **Commit:** `43741df4`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-07-11T20:39:40+05:30
- **Changes:** 35 files (+668/-7)

## 876. refactor: use `Debug` impl instead of `Display` impl for logging errors (#5301)

- **Commit:** `e835706a`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-07-12T13:21:22+05:30
- **Changes:** 27 files (+192/-153)

## 877. chore(euclid_wasm): refactor connector metadata (#5083)

- **Commit:** `8b614c9b`
- **Author:** Jeeva Ramachandran <120017870+JeevaRamu0104@users.noreply.github.com>
- **Date:** 2024-07-12T16:52:56+05:30
- **Changes:** 7 files (+3360/-1047)

## 878. chore: making of function create_encrypted_data (#5251)

- **Commit:** `6ee1cad4`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-07-12T18:34:57+05:30
- **Changes:** 8 files (+182/-127)

## 879. feat(connector): [DATATRANS] Implement card payments (#5028)

- **Commit:** `f24a4070`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-07-12T18:40:27+05:30
- **Changes:** 17 files (+4748/-193)

## 880. feat(payment_methods): add support to migrate existing customer PMs from processor to hyperswitch (#5306)

- **Commit:** `21499947`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2024-07-13T22:11:44+05:30
- **Changes:** 10 files (+422/-28)

## 881. feat(logging): Emit a setup error when a restricted keys are used for logging default keys (#5185)

- **Commit:** `ff96a62b`
- **Author:** Abhishek Kanojia <89402434+Abhitator216@users.noreply.github.com>
- **Date:** 2024-07-14T19:28:21+05:30
- **Changes:** 14 files (+151/-176)

## 882. feat(core): [Payouts] Add retrieve flow for payouts (#4936)

- **Commit:** `693f08dc`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-15T17:50:52+05:30
- **Changes:** 19 files (+511/-7)

## 883. feat(mca): Added recipient connector call for open banking connectors (#3758)

- **Commit:** `3951ac65`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-07-16T13:42:03+05:30
- **Changes:** 30 files (+1052/-27)

## 884. fix(database): modified_at updated for every state change for Payment Attempts (#5312)

- **Commit:** `926dcd3a`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-07-16T16:07:09+05:30
- **Changes:** 50 files (+1524/-242)

## 885. chore: create justfile for running commands for v1 and v2 migrations (#5325)

- **Commit:** `23bfceb6`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-07-16T17:27:34+05:30
- **Changes:** 15 files (+1544/-60)

## 886. feat(webhooks): add support for custom outgoing webhook http headers (#5275)

- **Commit:** `101b21f5`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-07-16T21:43:44+05:30
- **Changes:** 14 files (+363/-222)

## 887. refactor(connector): added amount conversion framework for checkout,adyen and globalpay (#4974)

- **Commit:** `ecc862c3`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-07-17T12:57:46+05:30
- **Changes:** 22 files (+415/-223)

## 888. feat(core): Payments core modification for open banking connectors (#3947)

- **Commit:** `eb6f27d6`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-07-17T14:57:50+05:30
- **Changes:** 101 files (+1101/-48)

## 889. feat(payout_link): secure payout links using server side validations and client side headers (#5219)

- **Commit:** `2d204c9f`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-07-17T18:23:55+05:30
- **Changes:** 23 files (+794/-348)

## 890. feat(connector): [Itau Bank] Template for payment flows (#5304)

- **Commit:** `ef1418f9`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-18T15:00:23+05:30
- **Changes:** 20 files (+1283/-6)

## 891. refactor(routing): Remove backwards compatibility for the routing crate (#3015)

- **Commit:** `78a7804b`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-07-18T15:13:38+05:30
- **Changes:** 122 files (+469/-1762)

## 892. build: remove unused dependencies (#5343)

- **Commit:** `7f582e47`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-07-18T18:51:42+05:30
- **Changes:** 31 files (+64/-190)

## 893. Docs: Updating Error codes for documentation purposes (#5314)

- **Commit:** `fe14336f`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-07-18T20:50:14+05:30
- **Changes:** 1 files (+333/-318)

## 894. feat: encryption service integration to support batch encryption and decryption (#5164)

- **Commit:** `33298b38`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2024-07-19T13:08:58+05:30
- **Changes:** 127 files (+4239/-1378)

## 895. feat(connector): Plaid connector Integration (#3952)

- **Commit:** `eb016802`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-07-19T13:35:27+05:30
- **Changes:** 26 files (+1403/-56)

## 896. feat(merchant_account_v2): add merchant_account_v2 domain and diesel models (#5365)

- **Commit:** `5861c5a6`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-07-19T19:09:31+05:30
- **Changes:** 40 files (+1124/-195)

## 897. fix: use encrypt api for all encryption and decryption (#5379)

- **Commit:** `83849a5f`
- **Author:** Arjun Karthik <m.arjunkarthik@gmail.com>
- **Date:** 2024-07-19T21:03:17+05:30
- **Changes:** 17 files (+117/-96)

## 898. refactor(router): Make `original_payment_authorized_currency` and `original_payment_authorized_amount` mandatory fields for `Discover` cards and `Cybersource` connector during payment method migration. (#5370)

- **Commit:** `06f1406c`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-07-22T12:38:44+05:30
- **Changes:** 3 files (+176/-145)

## 899. fix: add offset and limit to key transfer API (#5358)

- **Commit:** `b393803a`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-07-22T15:35:14+05:30
- **Changes:** 23 files (+1038/-927)

## 900. feat(connector): [Itau Bank] Add payment and sync flow for Pix (#5342)

- **Commit:** `3fef96e7`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-22T16:07:22+05:30
- **Changes:** 41 files (+768/-144)

## 901. feat(customer): customer v2 refactor for customer create end point (#5350)

- **Commit:** `aaf1f2b1`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-07-23T13:10:07+05:30
- **Changes:** 36 files (+965/-383)

## 902. Feat(connector): [WELLSFARGO] Add template code (#5333)

- **Commit:** `94bb3e78`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-07-23T20:41:08+05:30
- **Changes:** 23 files (+1324/-4)

## 903. feat: add create retrieve and update api endpoints for organization resource (#5361)

- **Commit:** `26b87830`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-07-24T12:10:37+05:30
- **Changes:** 44 files (+739/-180)

## 904. refactor(merchant_id): create domain type for `merchant_id` (#5408)

- **Commit:** `7068fbfb`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-07-24T19:18:25+05:30
- **Changes:** 406 files (+3175/-2640)

## 905. feat(connector): [Itaubank] Add refund and rsync flow  (#5420)

- **Commit:** `920b3236`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-24T20:09:41+05:30
- **Changes:** 18 files (+226/-202)

## 906. refactor(core): patch file for removal of id from schema (#5398)

- **Commit:** `ff3b9a2a`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-07-24T23:01:18+05:30
- **Changes:** 37 files (+127/-97)

## 907. feat(router): add merchant_connector_account create v2 api flow (#5385)

- **Commit:** `98349a0c`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-07-25T00:57:13+05:30
- **Changes:** 20 files (+1798/-813)

## 908. feat(connector): [HELCIM] Move connector to hyperswitch_connectors (#5287)

- **Commit:** `0f89a0ac`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-07-25T12:57:37+05:30
- **Changes:** 61 files (+3828/-1417)

## 909. refactor(user_roles): make org and merchant id nullable (#5353)

- **Commit:** `0330aff9`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-07-25T16:02:58+05:30
- **Changes:** 16 files (+546/-203)

## 910. refactor(merchant_account_v2): recreate id for `merchant_account` v2  (#5439)

- **Commit:** `93976db3`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-07-26T12:39:34+05:30
- **Changes:** 18 files (+398/-79)

## 911. feat(connector): [FISERV] Move connector to hyperswitch_connectors (#5441)

- **Commit:** `2bee694d`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-07-26T15:41:27+05:30
- **Changes:** 12 files (+400/-347)

## 912. feat(connector): [Bambora APAC] add mandate flow (#5376)

- **Commit:** `dbfa006b`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-07-26T18:45:23+05:30
- **Changes:** 8 files (+321/-24)

## 913. refactor(router): remove `connector_account_details` and `connector_webhook_details` in merchant_connector_account list response (#5457)

- **Commit:** `45a14941`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-07-29T14:37:16+05:30
- **Changes:** 6 files (+322/-3)

## 914. feat: rename columns in organization for v2 (#5424)

- **Commit:** `a791391e`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-07-30T12:45:48+05:30
- **Changes:** 20 files (+378/-77)

## 915. feat(payment_link): add provision for secured payment links (#5357)

- **Commit:** `043abb59`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-07-30T13:12:35+05:30
- **Changes:** 31 files (+841/-318)

## 916. feat(connector): [BAMBORA, BITPAY, STAX] Move connector to hyperswitch_connectors (#5450)

- **Commit:** `827fa074`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-07-30T17:34:41+05:30
- **Changes:** 21 files (+1191/-1030)

## 917. refactor(id_type): use macros for defining ID types and implementing common traits (#5471)

- **Commit:** `1d4fb1d2`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-07-30T20:21:29+05:30
- **Changes:** 34 files (+321/-384)

## 918. feat(connector): [Paybox] add connector template code (#5485)

- **Commit:** `5e1eb4af`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-08-01T12:24:54+05:30
- **Changes:** 24 files (+1311/-8)

## 919. feat(auth): Add support for partial-auth, by facilitating injection of authentication parameters in headers (#4802)

- **Commit:** `1d4c87a9`
- **Author:** Nishant Joshi <nishant.joshi@juspay.in>
- **Date:** 2024-08-01T14:57:39+05:30
- **Changes:** 31 files (+523/-103)

## 920. refactor(routing): Api v2 for routing create and activate endpoints (#5423)

- **Commit:** `6140cfe0`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-01T15:00:28+05:30
- **Changes:** 11 files (+568/-139)

## 921. refactor(router): domain and diesel model changes for merchant_connector_account create v2 flow (#5462)

- **Commit:** `85209d12`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-08-01T17:27:39+05:30
- **Changes:** 36 files (+2105/-472)

## 922. feat(business_profile): introduce domain models for business profile v1 and v2 APIs (#5497)

- **Commit:** `537630f0`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-01T19:14:21+05:30
- **Changes:** 17 files (+1458/-61)

## 923. refactor(payment_methods): List the Payment Methods for Merchant , based on the connector  type (#4909)

- **Commit:** `f3677f26`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-02T18:33:41+05:30
- **Changes:** 73 files (+2712/-8691)

## 924. refactor(router): refactor merchant_connector update v2 flow (#5484)

- **Commit:** `9e358e4f`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-08-05T13:38:48+05:30
- **Changes:** 6 files (+496/-156)

## 925. refactor(routing): Refactor api v2 routes for deactivating and retrieving the routing config (#5478)

- **Commit:** `3fea00c4`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-05T15:28:19+05:30
- **Changes:** 4 files (+168/-58)

## 926. feat(connector): Remove Braintree SDK Flow support (#5264)

- **Commit:** `61a0cb3e`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-08-06T14:49:38+05:30
- **Changes:** 12 files (+1843/-2752)

## 927. refactor(merchant_account_v2):  recreate id and remove deprecated fields from merchant account (#5493)

- **Commit:** `49892b26`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-06T15:05:40+05:30
- **Changes:** 26 files (+988/-671)

## 928. Feat(connector): [WELLSFARGO] Implement Payment Flows (#5463)

- **Commit:** `a0827596`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-08-06T20:49:41+05:30
- **Changes:** 20 files (+4551/-340)

## 929. refactor(core): Refactor customer payment method list for v2 (#4856)

- **Commit:** `83022724`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-08-06T20:55:30+05:30
- **Changes:** 11 files (+979/-116)

## 930. feat(customer_v2):  add customer create v2 endpoint  (#5444)

- **Commit:** `52cada01`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-08-07T13:12:10+05:30
- **Changes:** 47 files (+1473/-159)

## 931. refactor(business_profile): use concrete types for JSON fields (#5531)

- **Commit:** `a8ba21c1`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-07T13:57:35+05:30
- **Changes:** 18 files (+751/-606)

## 932. refactor(router): refactor `merchant_connector_account` retrieve and delete v2 apis (#5528)

- **Commit:** `253f1be3`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-08-07T17:10:27+05:30
- **Changes:** 10 files (+345/-69)

## 933. feat(core): add support for payment links localization (#5530)

- **Commit:** `3604b4ff`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-08-07T17:41:43+05:30
- **Changes:** 28 files (+702/-70)

## 934. feat: add a wrapper for encryption and decryption (#5502)

- **Commit:** `f51b6c91`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-08-07T17:50:36+05:30
- **Changes:** 30 files (+746/-358)

## 935. refactor: use business profile domain models instead of diesel models (#5566)

- **Commit:** `e56ad0d6`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-08T15:39:02+05:30
- **Changes:** 69 files (+913/-990)

## 936. feat: payment processor token for recurring payments (#5508)

- **Commit:** `0cbbc92a`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-08-08T19:39:46+05:30
- **Changes:** 17 files (+210/-27)

## 937. feat(core): [Payment Link] add dynamic merchant fields (#5512)

- **Commit:** `03f0ea15`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-08-08T19:50:07+05:30
- **Changes:** 11 files (+160/-41)

## 938. feat(core): use profile_id passed from auth layer within core functions (#5553)

- **Commit:** `9fa631d2`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-08-09T12:28:47+05:30
- **Changes:** 12 files (+233/-32)

## 939. refactor(core): Use hyperswitch_domain_models within the Payments Core instead of api_models (#5511)

- **Commit:** `f81416e4`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2024-08-09T14:45:15+05:30
- **Changes:** 73 files (+729/-435)

## 940. refactor(connector): connector template generation (#5568)

- **Commit:** `8fdcabda`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-08-09T17:12:47+05:30
- **Changes:** 3 files (+174/-137)

## 941. refactor(payouts): openAPI schemas and mintlify docs (#5284)

- **Commit:** `942e63d9`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-08-09T18:18:43+05:30
- **Changes:** 31 files (+1709/-843)

## 942. refactor(openapi): add openapi support for generating v2 api-reference (#5580)

- **Commit:** `92d76a36`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-08-09T20:30:59+05:30
- **Changes:** 14 files (+17853/-15)

## 943. refactor(merchant_account_v2): remove routing algorithms from merchant account and add version column (#5527)

- **Commit:** `f1196be9`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-10T11:50:31+05:30
- **Changes:** 26 files (+260/-132)

## 944. feat(payout_link): add localisation support for payout link's templates (#5552)

- **Commit:** `b0346e08`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-08-12T13:12:54+05:30
- **Changes:** 40 files (+1077/-84)

## 945. feat(connector): [WELLSFARGO_PAYOUT] PR template code (#5567)

- **Commit:** `6a5b4939`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-08-12T13:14:10+05:30
- **Changes:** 22 files (+1305/-4)

## 946. refactor(core): Adapt the usage of routing_algorithm_id in routing and payments core for v2 (#5533)

- **Commit:** `61de3e02`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-12T14:56:51+05:30
- **Changes:** 21 files (+899/-437)

## 947. feat: change admin api key auth to merchant api key auth in few connectors flow (#5572)

- **Commit:** `7a23e663`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-08-12T14:57:23+05:30
- **Changes:** 12 files (+239/-19)

## 948. build: bump MSRV to 1.76.0 (#5586)

- **Commit:** `59b36a05`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-12T15:30:05+05:30
- **Changes:** 90 files (+255/-260)

## 949. feat(connector): [FISERVEMEA] Add template code (#5583)

- **Commit:** `74fcc910`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-08-12T16:01:47+05:30
- **Changes:** 25 files (+1304/-4)

## 950. refactor(openapi_v2): add merchant account v2 openapi (#5588)

- **Commit:** `c8943eb2`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-12T18:19:08+05:30
- **Changes:** 32 files (+1085/-77)

## 951. refactor(routing): Refactor fallback routing apis for v2 (#5592)

- **Commit:** `051086f7`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-13T18:01:33+05:30
- **Changes:** 9 files (+352/-57)

## 952. feat(connector): create Taxjar connector (#5597)

- **Commit:** `0ab0aa1a`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2024-08-13T22:18:56+05:30
- **Changes:** 25 files (+1344/-54)

## 953. refactor(webhook_events): allow listing unique webhook events based on profile ID (#5598)

- **Commit:** `8bcda2ce`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-14T14:56:18+05:30
- **Changes:** 15 files (+233/-298)

## 954. feat(customer_v2): customer v2 refactor customer v2 update endpoint (#5490)

- **Commit:** `17703fe2`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-08-14T14:56:34+05:30
- **Changes:** 28 files (+1714/-669)

## 955. feat(connector): [Paybox] add paybox connector (#5575)

- **Commit:** `e4f4fbaf`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-08-14T20:01:22+05:30
- **Changes:** 17 files (+962/-182)

## 956. feat(payout_link): return total_count in filtered payouts list API response (#5538)

- **Commit:** `34f648e2`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-08-14T20:03:10+05:30
- **Changes:** 11 files (+349/-37)

## 957. feat(users): add support for profile user delete (#5541)

- **Commit:** `19a91809`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-08-14T20:04:11+05:30
- **Changes:** 5 files (+384/-114)

## 958. refactor(router): add api_version and make profile_id mandatory in mca v2 (#5602)

- **Commit:** `56791c27`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-08-14T20:49:26+05:30
- **Changes:** 25 files (+108/-130)

## 959. feat(business_profile_v2): business profile v2 create and retrieve endpoint (#5606)

- **Commit:** `6e7b38a6`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-20T14:50:58+05:30
- **Changes:** 28 files (+756/-248)

## 960. feat(core): [Payouts] add merchant_connector_id to payout_attempt and show in response (#5214)

- **Commit:** `4cc389aa`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-08-20T21:45:33+05:30
- **Changes:** 9 files (+154/-152)

## 961. feat(business_profile): introduce business profile v2 update endpoint (#5641)

- **Commit:** `beb4fb05`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-21T14:27:18+05:30
- **Changes:** 23 files (+689/-223)

## 962. feat: use admin_api_key auth along with merchant_id for connector list, retrieve and update apis (#5613)

- **Commit:** `b60ced02`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-08-21T14:53:10+05:30
- **Changes:** 13 files (+135/-226)

## 963. chore: generate openapi specs for organization endpoint for v1 and v2 (#5648)

- **Commit:** `1d08c7b9`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-08-21T16:45:45+05:30
- **Changes:** 8 files (+214/-6)

## 964. feat(core): add localization support for unified error messages (#5624)

- **Commit:** `1f0ee3ca`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-08-21T18:05:44+05:30
- **Changes:** 23 files (+525/-9)

## 965. feat(user_role): Add update by lineage DB function (#5651)

- **Commit:** `ca72feda`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-08-22T10:30:07+05:30
- **Changes:** 9 files (+571/-605)

## 966. feat(user): add list org, merchant and profile api (#5662)

- **Commit:** `98cbf2e7`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-08-22T14:34:32+05:30
- **Changes:** 9 files (+445/-4)

## 967. refactor(core):  Refactor fallback routing behaviour in payments for v2 (#5642)

- **Commit:** `22743ac3`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-22T15:56:15+05:30
- **Changes:** 14 files (+368/-241)

## 968. feat: add new routes for profile level list apis (#5589)

- **Commit:** `d3521e7e`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-08-22T17:02:38+05:30
- **Changes:** 10 files (+509/-0)

## 969. feat(router): collect customer address details based on business profile config regardless of connector required fields (#5418)

- **Commit:** `bda29cb1`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-08-22T17:09:14+05:30
- **Changes:** 18 files (+638/-767)

## 970. feat(global_id): create a `GlobalId` domain type (#5644)

- **Commit:** `d14c7887`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-22T17:23:08+05:30
- **Changes:** 3 files (+265/-15)

## 971. fix(router): [Adyen]  prevent partial submission of billing address and add required fields for all payment methods (#5660)

- **Commit:** `6d606179`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-08-22T18:39:28+05:30
- **Changes:** 2 files (+2304/-148)

## 972. feat(customer_v2): add route for customer retrieve v2  (#5516)

- **Commit:** `914cab0d`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-08-22T20:24:56+05:30
- **Changes:** 14 files (+247/-74)

## 973. feat(connector): [Adyen] add dispute flows for adyen connector (#5514)

- **Commit:** `ad9f91b3`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-08-23T12:13:38+05:30
- **Changes:** 16 files (+801/-126)

## 974. feat(payment_methods_v2): Payment methods v2 API models (#5564)

- **Commit:** `e98ff95b`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-08-26T12:19:22+05:30
- **Changes:** 18 files (+1632/-253)

## 975. refactor(payments_response): remove setter from payments response (#5676)

- **Commit:** `800da6a1`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-26T12:19:54+05:30
- **Changes:** 12 files (+507/-255)

## 976. build(deps): bump `diesel` to `2.2.3` and `sqlx` to `0.8.1` (#5688)

- **Commit:** `138134df`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-26T18:59:09+05:30
- **Changes:** 17 files (+272/-223)

## 977. feat: populate payment method details in payments response (#5661)

- **Commit:** `32db5dd1`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-08-26T22:01:35+05:30
- **Changes:** 10 files (+1958/-100)

## 978. feat(connector): [NOVALNET] Add template code (#5670)

- **Commit:** `c3c9b274`
- **Author:** dg-212 <debarati.ghatak@juspay.in>
- **Date:** 2024-08-27T12:23:30+05:30
- **Changes:** 25 files (+1298/-4)

## 979. feat(openapi):  Add open api routes for routing v2 (#5686)

- **Commit:** `6bb97671`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-08-27T13:23:46+05:30
- **Changes:** 16 files (+665/-23)

## 980. refactor: introduce a domain type for profile ID (#5687)

- **Commit:** `b63d723b`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-08-27T13:31:01+05:30
- **Changes:** 118 files (+707/-547)

## 981. feat: add test_mode for quickly testing payout links (#5669)

- **Commit:** `406256c0`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-08-27T13:33:03+05:30
- **Changes:** 11 files (+183/-90)

## 982. feat(connector): [NEXIXPAY] Add template code (#5684)

- **Commit:** `303684d1`
- **Author:** mrudul4935 <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2024-08-28T13:06:35+05:30
- **Changes:** 25 files (+1304/-8)

## 983. refactor(router): add domain type for merchant_connector_account id (#5685)

- **Commit:** `771f48cf`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-08-28T13:22:19+05:30
- **Changes:** 69 files (+388/-271)

## 984. feat(user_roles): support switch for new hierarchy (#5692)

- **Commit:** `53b31638`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-08-28T13:30:07+05:30
- **Changes:** 11 files (+559/-27)

## 985. refactor(customer_v2): fixed customer_v2 create panic issue (#5699)

- **Commit:** `c555a88c`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-08-28T13:42:41+05:30
- **Changes:** 24 files (+325/-82)

## 986. feat(connector): [FISERVEMEA] Integrate cards (#5672)

- **Commit:** `32dd3f97`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-08-28T15:16:32+05:30
- **Changes:** 23 files (+1005/-180)

## 987. feat(users): Add API to list users in user lineage (#5722)

- **Commit:** `20f20da9`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-08-28T17:29:41+05:30
- **Changes:** 18 files (+412/-48)

## 988. fix(router): [Stripe/Itau/Paypal/Bambora/Cybs] prevent partial submission of billing address and add required fields for all payment methods (#5704)

- **Commit:** `c85b4a3a`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-08-28T18:45:05+05:30
- **Changes:** 7 files (+797/-193)

## 989. feat(api_keys): add api keys route to api v2 (#5709)

- **Commit:** `089a9506`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-08-28T18:57:36+05:30
- **Changes:** 20 files (+865/-426)

## 990. feat(connector): [FIUU] PR template code  (#5691)

- **Commit:** `3f17b52a`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-08-29T12:15:06+05:30
- **Changes:** 24 files (+1299/-5)

## 991. feat(database): add profile & organisation id to transaction tables (#5696)

- **Commit:** `2049ab05`
- **Author:** Sampras Lopes <Sampras.lopes@juspay.in>
- **Date:** 2024-08-29T15:06:44+05:30
- **Changes:** 39 files (+553/-92)

## 992. feat(user_role): Insert V2 user_roles (#5607)

- **Commit:** `6c266b5d`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-08-29T20:12:04+05:30
- **Changes:** 7 files (+474/-141)

## 993. refactor(router): revert [Stripe/Itau/Paypal/Bambora/Cybs] prevent partial submission of billing address and add required fields for all payment methods (#5745)

- **Commit:** `18f912de`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-08-29T21:16:56+05:30
- **Changes:** 7 files (+190/-794)

## 994. refactor(core): make the ppt token flow to accept optional mca_id (#5744)

- **Commit:** `f682b570`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-08-30T18:11:37+05:30
- **Changes:** 5 files (+130/-81)

## 995. refactor(users): Add V2 user_roles data support (#5763)

- **Commit:** `6b410505`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-09-01T19:09:25+05:30
- **Changes:** 31 files (+768/-2042)

## 996. refactor(payment_id): add payment id domain type (#5738)

- **Commit:** `7296cceb`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-09-02T09:21:33+05:30
- **Changes:** 150 files (+880/-803)

## 997. feat(roles): add list support for roles (#5754)

- **Commit:** `e4f1fbc5`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-09-02T12:12:50+05:30
- **Changes:** 13 files (+396/-23)

## 998. refactor(business_profile): change id for business profile (#5748)

- **Commit:** `8e5c33e2`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-09-02T15:25:22+05:30
- **Changes:** 27 files (+538/-274)

## 999. refactor(connector): Move globepay, powertranz, tsys, worldline to hyperswitch_connectors (#5758)

- **Commit:** `1d149716`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-09-02T16:48:58+05:30
- **Changes:** 18 files (+1410/-1451)

## 1000. refactor(v2_migrations): re-organize v2 migrations (#5760)

- **Commit:** `f32a3294`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-09-02T18:31:39+05:30
- **Changes:** 46 files (+367/-404)

## 1001. feat(connector): [Adyenplatform] add webhooks for payout (#5749)

- **Commit:** `258212d8`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-09-02T19:22:09+05:30
- **Changes:** 2 files (+242/-13)

## 1002. feat(user): implement invitations api (#5769)

- **Commit:** `730c2ba2`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-09-02T20:29:36+05:30
- **Changes:** 11 files (+240/-146)

## 1003. feat(connector): [DEUTSCHE] Add template code (#5774)

- **Commit:** `42f945fd`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-09-03T15:50:48+05:30
- **Changes:** 25 files (+1312/-8)

## 1004. fix(router): make customer details None in the `Psync` flow if the customer is deleted (#5732)

- **Commit:** `98cfc13f`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-09-03T15:52:35+05:30
- **Changes:** 5 files (+244/-23)

## 1005. feat(analytics): refactor and introduce analytics APIs to accommodate OrgLevel, MerchantLevel and ProfileLevel authentication (#5729)

- **Commit:** `8ed942c6`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-09-03T15:53:04+05:30
- **Changes:** 63 files (+2908/-1555)

## 1006. refactor(euclid): check the authenticity of profile_id being used (#5647)

- **Commit:** `0fb8e85e`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-09-03T18:28:15+05:30
- **Changes:** 6 files (+329/-59)

## 1007. feat(revert): populate payment method details in payments response (#5785)

- **Commit:** `c84af20e`
- **Author:** Sampras Lopes <Sampras.lopes@juspay.in>
- **Date:** 2024-09-04T12:58:36+05:30
- **Changes:** 10 files (+100/-1958)

## 1008. refactor(router): remove admin v2 intermediate features (#5780)

- **Commit:** `b8532261`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-09-04T13:58:05+05:30
- **Changes:** 71 files (+458/-1351)

## 1009. feat(payment_methods_v2): Implemented Diesel and Domain models for v2 (#5700)

- **Commit:** `c3cc887e`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-09-04T18:00:42+05:30
- **Changes:** 39 files (+2713/-669)

## 1010. Feat(connector): [Fiuu] Add Card Flows (#5786)

- **Commit:** `ed0d8162`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-09-04T19:53:22+05:30
- **Changes:** 20 files (+1489/-266)

## 1011. feat(users): Add profile level invites (#5793)

- **Commit:** `28e7a7fc`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-09-04T20:26:50+05:30
- **Changes:** 19 files (+685/-393)

## 1012. feat(user_roles): get user role details (#5777)

- **Commit:** `eae8d891`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-09-05T01:42:20+05:30
- **Changes:** 5 files (+275/-6)

## 1013. feat(customer_v2): Add customer V2 delete api (#5518)

- **Commit:** `a901d671`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-09-05T14:52:43+05:30
- **Changes:** 24 files (+691/-212)

## 1014. feat(users): Send profile_id in JWT and user_info APIs (#5817)

- **Commit:** `4d499038`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-09-05T19:01:24+05:30
- **Changes:** 9 files (+111/-130)

## 1015. feat(user): implement entity level authorization (#5819)

- **Commit:** `e15ea184`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-09-05T23:08:35+05:30
- **Changes:** 25 files (+806/-246)

## 1016. feat(core): Add Support for Payments Dynamic Tax Calculation Based on Shipping Address (#5619)

- **Commit:** `a03ad53e`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-09-06T19:08:15+05:30
- **Changes:** 75 files (+2930/-1237)

## 1017. feat(recon): add merchant and profile IDs in auth tokens (#5643)

- **Commit:** `d9485a5f`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-09-06T19:55:40+05:30
- **Changes:** 30 files (+336/-336)

## 1018. feat: enable payment and refund filter at DB query level (#5827)

- **Commit:** `21352cf8`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-09-09T13:23:47+05:30
- **Changes:** 14 files (+268/-60)

## 1019. feat(analytics): Revert api_event metrics and filters back to merchant_id authentication (#5821)

- **Commit:** `283154d3`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-09-10T13:30:26+05:30
- **Changes:** 8 files (+65/-208)

## 1020. feat(connector): [THUNES] Add template code (#5775)

- **Commit:** `9b508a83`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2024-09-10T16:03:50+05:30
- **Changes:** 23 files (+1277/-4)

## 1021. feat(payout): add dynamic fields for payout links (#5764)

- **Commit:** `f4ad6579`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-09-10T16:32:52+05:30
- **Changes:** 24 files (+1005/-65)

## 1022. feat(users): New profile level roles (#5843)

- **Commit:** `3cb0f240`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-09-10T17:55:03+05:30
- **Changes:** 9 files (+195/-57)

## 1023. fix(router): [Stripe/Itau/Paypal/Bambora/Cybersource] prevent partial submission of billing address and add required fields for all payment methods (#5752)

- **Commit:** `ad40cedf`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-09-10T18:11:46+05:30
- **Changes:** 8 files (+1061/-295)

## 1024. feat(core): [Payouts] Add billing address to payout list (#5004)

- **Commit:** `49a60bf1`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-09-10T22:32:22+05:30
- **Changes:** 9 files (+240/-91)

## 1025. refactor: Add a GAT Data to Operation trait (#5825)

- **Commit:** `418ea4e2`
- **Author:** Arun Raj M <jarnura47@gmail.com>
- **Date:** 2024-09-11T10:55:01+05:30
- **Changes:** 55 files (+1903/-1194)

## 1026. feat(payment_method_data): populate additional payment method data fields across all the methods in payments response (#5788)

- **Commit:** `034f736e`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-09-11T11:30:59+05:30
- **Changes:** 16 files (+2572/-120)

## 1027. Feat(connector): [Fiuu] Add DuitNow/FPX PaymentMethod (#5841)

- **Commit:** `8c0fec9d`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-09-11T16:29:18+05:30
- **Changes:** 22 files (+365/-156)

## 1028. feat(connector): [Novalnet] add Payment flows for cards (#5726)

- **Commit:** `246fdc84`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-09-12T12:17:38+05:30
- **Changes:** 24 files (+1714/-141)

## 1029. refactor(payment_links): Update API contract for dynamic transaction details and upgrade UI (#5849)

- **Commit:** `a96e9f3e`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-09-12T18:58:21+05:30
- **Changes:** 10 files (+210/-42)

## 1030. feat(refunds): Refunds aggregate api (#5795)

- **Commit:** `00386f32`
- **Author:** Gitanjli <96485413+gitanjli525@users.noreply.github.com>
- **Date:** 2024-09-12T18:59:25+05:30
- **Changes:** 14 files (+229/-4)

## 1031. refactor(core): Update shipping_cost and order_tax_amount to net_amount of payment_attempt (#5844)

- **Commit:** `840609af`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-09-12T22:48:12+05:30
- **Changes:** 49 files (+681/-204)

## 1032. feat(payments_v2): payment intent diesel and domain models changes v2 (#5783)

- **Commit:** `10ac0894`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-09-13T13:11:38+05:30
- **Changes:** 59 files (+2987/-856)

## 1033. feat(connector): [DEUTSCHEBANK] Integrate SEPA Payments (#5826)

- **Commit:** `6fc20606`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-09-13T16:59:33+05:30
- **Changes:** 31 files (+1157/-196)

## 1034. refactor(user_roles): Populate role names and entity names in user role APIs (#5861)

- **Commit:** `4d28cf27`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-09-13T18:26:26+05:30
- **Changes:** 12 files (+373/-100)

## 1035. refactor(payment_methods): unify locker api function call (#5863)

- **Commit:** `4137d7b4`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-09-16T12:19:49+05:30
- **Changes:** 6 files (+181/-88)

## 1036. feat(router): Default configs and toggle api for dynamic routing feature (#5830)

- **Commit:** `9f9a4140`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-09-16T12:23:32+05:30
- **Changes:** 26 files (+996/-41)

## 1037. feat(core): Add support for card network tokenization (#5599)

- **Commit:** `61e2ca9b`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2024-09-16T16:43:15+05:30
- **Changes:** 63 files (+2360/-215)

## 1038. feat(router): add admin list apis for v2 (#5883)

- **Commit:** `bc6c460c`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-09-17T13:38:46+05:30
- **Changes:** 20 files (+474/-34)

## 1039. refactor: add encryption support to payment attempt domain model (#5882)

- **Commit:** `f72abe4b`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-09-17T16:26:08+05:30
- **Changes:** 30 files (+2929/-678)

## 1040. refactor(connector): Move connector Volt and Mollie from Router to HyperswitchConnector Trait (#5612)

- **Commit:** `1d9e6396`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-09-17T20:53:54+05:30
- **Changes:** 14 files (+646/-688)

## 1041. feat(payment_methods_v2): Payment method Create API (#5812)

- **Commit:** `be902ffa`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-09-18T12:22:09+05:30
- **Changes:** 35 files (+2168/-798)

## 1042. feat(disputes): add support for disputes aggregate (#5896)

- **Commit:** `0a0c93e1`
- **Author:** Riddhiagrawal001 <50551695+Riddhiagrawal001@users.noreply.github.com>
- **Date:** 2024-09-18T12:24:42+05:30
- **Changes:** 11 files (+247/-2)

## 1043. docs: add openapi docs for customers v2 (#5926)

- **Commit:** `2bc8756e`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-09-18T12:24:55+05:30
- **Changes:** 3 files (+339/-0)

## 1044. feat(routing): build gRPC Client Interface to initiate communication with other gRPC services (#5835)

- **Commit:** `99f59338`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-09-18T13:52:19+05:30
- **Changes:** 24 files (+691/-33)

## 1045. feat(payments): store and propagate additional wallet pm details in payments response (#5869)

- **Commit:** `8320dc07`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-09-19T18:54:56+05:30
- **Changes:** 7 files (+205/-7)

## 1046. feat(payout): add unified error code and messages along with translation (#5810)

- **Commit:** `a0f4bb77`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-09-19T18:55:12+05:30
- **Changes:** 24 files (+605/-80)

## 1047. feat(connector): [Novalnet] add Recurring payment flow for cards (#5921)

- **Commit:** `6a6ce175`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-09-19T18:55:57+05:30
- **Changes:** 4 files (+514/-119)

## 1048. fix(payments): add time range in list payment attempts query (#5959)

- **Commit:** `156a161f`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-09-19T23:19:47+05:30
- **Changes:** 40 files (+111/-96)

## 1049. refactor: Rename business profile to profiles in api, diesel, domain, interface and error types (#5877)

- **Commit:** `dee91b36`
- **Author:** Arun Raj M <jarnura47@gmail.com>
- **Date:** 2024-09-19T23:30:25+05:30
- **Changes:** 99 files (+2643/-2655)

## 1050. feat(connector): [DEUTSCHEBANK] Implement SEPA recurring payments (#5925)

- **Commit:** `00e913c7`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-09-20T16:46:57+05:30
- **Changes:** 34 files (+300/-68)

## 1051. refactor(payment_intent_v2): payment intent fields refactoring (#5880)

- **Commit:** `5335f2d2`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-09-20T16:50:53+05:30
- **Changes:** 48 files (+2526/-1668)

## 1052. feat(router): add support for Samsung Pay payment method (#5955)

- **Commit:** `fe15cc79`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-09-20T16:56:24+05:30
- **Changes:** 27 files (+997/-46)

## 1053. refactor(open_banking): Refactored to consume and use headers from SDK (#5884)

- **Commit:** `d9270ace`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-09-20T21:21:17+05:30
- **Changes:** 44 files (+251/-59)

## 1054. feat(disputes): add filters for disputes list (#5637)

- **Commit:** `365f5680`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-09-22T23:39:37+05:30
- **Changes:** 14 files (+446/-125)

## 1055. refactor(connector): Move cashtocode,coinbase,cryptopay to crate hyperswitch_connectors (#5983)

- **Commit:** `371ed5de`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-09-24T13:49:28+05:30
- **Changes:** 15 files (+633/-706)

## 1056. feat(router): add api_models and openapi changes for payments create intent api for v2 (#5971)

- **Commit:** `dc6208c5`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-09-24T13:49:50+05:30
- **Changes:** 11 files (+914/-13)

## 1057. feat(users): Add entity type filter in list users and list roles API (#5997)

- **Commit:** `3ddfe538`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-09-24T19:48:39+05:30
- **Changes:** 7 files (+180/-86)

## 1058. chore: address some clippy lints arising from v2 code (#6015)

- **Commit:** `dec0a57f`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-09-25T16:21:27+05:30
- **Changes:** 16 files (+115/-112)

## 1059. fix(api_key): fix api key `list` and `update` endpoints for v2 (#5980)

- **Commit:** `cda690bf`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2024-09-25T16:22:09+05:30
- **Changes:** 12 files (+214/-47)

## 1060. feat(router): add payment_intent_data and modify api models of create intent request and response for v2 (#6016)

- **Commit:** `9a605afe`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-09-25T23:29:33+05:30
- **Changes:** 5 files (+321/-137)

## 1061. feat(routing): success based routing metrics (#5951)

- **Commit:** `809c92bd`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-09-26T12:47:00+05:30
- **Changes:** 14 files (+601/-21)

## 1062. feat(payment_methods_v2): Update and Retrieve payment method APIs for v2 (#5939)

- **Commit:** `f0969922`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-09-26T18:45:18+05:30
- **Changes:** 10 files (+432/-67)

## 1063. fix(users): remove internal entity type for users (#6013)

- **Commit:** `991ca38b`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-09-26T19:32:21+05:30
- **Changes:** 10 files (+180/-246)

## 1064. feat(router): add support for co-badged cards (#5801)

- **Commit:** `0add2093`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-09-26T22:00:44+05:30
- **Changes:** 12 files (+394/-150)

## 1065. feat(core): [Payouts] Add payout_method_details to response (#5887)

- **Commit:** `5912936f`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-09-26T22:25:06+05:30
- **Changes:** 20 files (+1339/-11)

## 1066. feat(router): revert support for co-badged cards (#6142)

- **Commit:** `8d5ad1ec`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-09-27T17:37:41+05:30
- **Changes:** 12 files (+150/-394)

## 1067. feat(connector): [Paybox] Add 3DS Flow (#6088)

- **Commit:** `354f5306`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-09-27T18:50:29+05:30
- **Changes:** 15 files (+681/-66)

## 1068. refactor(payment_attempt_v2): add payment attempt v2 domain and diesel models (#6027)

- **Commit:** `c7bb9ccd`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-09-27T18:52:40+05:30
- **Changes:** 56 files (+2589/-1996)

## 1069. refactor(connector): Move connector Dlocal and Square from router to hyperswitch_connector crate (#6156)

- **Commit:** `05080259`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2024-10-01T15:55:43+05:30
- **Changes:** 12 files (+686/-748)

## 1070. feat(connector): [Nexixpay] add Payment & Refunds flows for cards (#5864)

- **Commit:** `602f50b9`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2024-10-02T21:34:37+05:30
- **Changes:** 31 files (+1783/-172)

## 1071. fix(payment_intent): batch encrypt and decrypt payment intent (#6164)

- **Commit:** `369939a3`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-10-03T12:16:28+05:30
- **Changes:** 4 files (+190/-93)

## 1072. feat(connector): [Digital Virgo] template for integration (#6145)

- **Commit:** `be3cf2c8`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-10-03T15:03:12+05:30
- **Changes:** 25 files (+1278/-13)

## 1073. feat(connector): add dynamic duitnow qr code, google pay and applpe pay  for fiuu (#6204)

- **Commit:** `2e54186a`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-10-04T14:11:59+05:30
- **Changes:** 6 files (+634/-168)

## 1074. fix(router): Persist card_network if present for non co-badged cards (#6212)

- **Commit:** `75648262`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-10-04T15:06:14+05:30
- **Changes:** 13 files (+383/-147)

## 1075. refactor(users): Deprecate unused user APIs and stabilize v1 APIs (#6114)

- **Commit:** `b2eb56e8`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-10-04T16:59:11+05:30
- **Changes:** 18 files (+80/-1260)

## 1076. refactor(user_role): Remove V1 insertion for `user_roles` and allow Invites for `org_admins` (#6185)

- **Commit:** `c07ee28c`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-10-04T16:59:34+05:30
- **Changes:** 6 files (+97/-247)

## 1077. feat(opensearch): restrict search view access based on user roles and permissions (#5932)

- **Commit:** `caa06931`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-10-04T18:51:30+05:30
- **Changes:** 4 files (+172/-42)

## 1078. fix: batch encrypt/decrypt on merchant connector account (#6206)

- **Commit:** `b7139483`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-10-04T18:55:20+05:30
- **Changes:** 3 files (+312/-268)

## 1079. feat(connector): [Novalnet] add webhooks for card (#6033)

- **Commit:** `d61ebef1`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-10-08T14:52:38+05:30
- **Changes:** 5 files (+319/-78)

## 1080. feat(connector): Integrate PAZE Wallet (#6030)

- **Commit:** `535f2f12`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2024-10-08T18:47:59+05:30
- **Changes:** 67 files (+837/-85)

## 1081. refactor(router): modify `net_amount` to be a struct in the domain model of payment_attempt and handle amount changes across all flows (#6252)

- **Commit:** `59300896`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-10-10T18:27:14+05:30
- **Changes:** 36 files (+830/-1134)

## 1082. feat(router): add network transaction id support for mit payments (#6245)

- **Commit:** `ba75a3f5`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-10-10T20:33:12+05:30
- **Changes:** 65 files (+1768/-247)

## 1083. feat(payment_methods_v2): Delete payment method api (#6211)

- **Commit:** `8e538cd6`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-10-14T15:42:55+05:30
- **Changes:** 8 files (+405/-245)

## 1084. feat(router): add support for Samsung pay app tokens flow (#6257)

- **Commit:** `f6b0b98e`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-10-14T15:45:55+05:30
- **Changes:** 8 files (+264/-40)

## 1085. feat(analytics): Add metrics, filters and APIs for Analytics v2 Dashboard - Payments Page (#5870)

- **Commit:** `f123df9a`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-10-14T18:43:34+05:30
- **Changes:** 55 files (+4353/-75)

## 1086. feat(core): add payments post_session_tokens flow (#6202)

- **Commit:** `53e82c3f`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-10-15T18:29:16+05:30
- **Changes:** 41 files (+1572/-108)

## 1087. feat(router): implement post_update_tracker for SessionUpdate Flow and add support for session_update_flow for Paypal (#6299)

- **Commit:** `7e90031c`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-10-15T23:38:44+05:30
- **Changes:** 29 files (+541/-136)

## 1088. feat(connector): [fiuu] Add support for payment and refund webhooks (#6315)

- **Commit:** `d04a87be`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-10-16T19:21:46+05:30
- **Changes:** 5 files (+478/-59)

## 1089. fix(users): Add max wrong attempts for two-fa (#6247)

- **Commit:** `2798f575`
- **Author:** Riddhiagrawal001 <50551695+Riddhiagrawal001@users.noreply.github.com>
- **Date:** 2024-10-17T12:56:52+05:30
- **Changes:** 8 files (+224/-5)

## 1090. feat(router): add payments create-intent flow for v2 (#6193)

- **Commit:** `afa803e0`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-10-17T15:50:47+05:30
- **Changes:** 64 files (+2004/-282)

## 1091. feat(worldpay): migrate to v7 (#6109)

- **Commit:** `962afbd0`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-10-17T15:51:59+05:30
- **Changes:** 66 files (+1490/-750)

## 1092. fix(mandates): handle the connector_mandate creation once and only if the payment is charged (#6327)

- **Commit:** `e14a0fe8`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-10-17T19:29:13+05:30
- **Changes:** 21 files (+366/-208)

## 1093. refactor(connector): [Billwerk] Move connector Billwerk form Router to HyperswitchConnector Crate (#6266)

- **Commit:** `3cf62101`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2024-10-18T18:48:47+05:30
- **Changes:** 8 files (+318/-314)

## 1094. feat(opensearch): add additional global search filters and create sessionizer indexes for local (#6352)

- **Commit:** `2e6cd6d3`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-10-19T19:27:53+05:30
- **Changes:** 9 files (+211/-9)

## 1095. refactor(connector): [WorldPay] migrate from modular to standard payment APIs (#6317)

- **Commit:** `58296ffa`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-10-21T15:29:44+05:30
- **Changes:** 12 files (+531/-268)

## 1096. refactor(router): Introduce ApiKeyId id type (#6324)

- **Commit:** `b3ce373f`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2024-10-21T19:19:31+05:30
- **Changes:** 14 files (+166/-75)

## 1097. feat(connector): add 3DS flow for Worldpay (#6374)

- **Commit:** `b93c8496`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-10-21T19:19:44+05:30
- **Changes:** 8 files (+583/-112)

## 1098. feat(analytics): remove additional filters from PaymentIntentFilters (#6403)

- **Commit:** `4ef48c39`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-10-23T11:54:48+05:30
- **Changes:** 19 files (+2/-361)

## 1099. feat(router): add api_models and openapi changes for refunds create api v2 (#6385)

- **Commit:** `5a10e586`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-10-23T16:53:46+05:30
- **Changes:** 15 files (+469/-38)

## 1100. refactor(connector):  Move connectors Forte, Nexinets, Payeezy, Payu and Zen from Router to Hyperswitch Connector Trait (#6261)

- **Commit:** `829a20cc`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2024-10-23T17:56:24+05:30
- **Changes:** 21 files (+1912/-1947)

## 1101. feat(payments_v2): add payment_confirm_intent api endpoint (#6263)

- **Commit:** `c7c1e1ad`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-10-24T16:10:01+05:30
- **Changes:** 125 files (+4785/-4336)

## 1102. feat(connector): [Novalnet] Integrate wallets Paypal and Googlepay (#6370)

- **Commit:** `673b8691`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-10-24T17:54:59+05:30
- **Changes:** 5 files (+285/-23)

## 1103. feat(authz): Create a permission generator (#6394)

- **Commit:** `4a0afb82`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-10-24T18:45:21+05:30
- **Changes:** 32 files (+646/-623)

## 1104. chore: address Rust 1.82.0 clippy lints (#6401)

- **Commit:** `8708a5cb`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2024-10-24T21:06:07+05:30
- **Changes:** 113 files (+668/-647)

## 1105. feat(connector): [Novalnet] Integrate Applepay wallet token flow (#6409)

- **Commit:** `1d24b045`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-10-25T15:58:15+05:30
- **Changes:** 5 files (+200/-39)

## 1106. feat(euclid): add dynamic routing in core flows (#6333)

- **Commit:** `ce732db9`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-10-25T16:38:38+05:30
- **Changes:** 11 files (+605/-492)

## 1107. feat(connector): [Fiuu] Add support for cards recurring payments (#6361)

- **Commit:** `4647a2f6`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-10-25T18:24:22+05:30
- **Changes:** 11 files (+798/-70)

## 1108. refactor(connector): added amount conversion framework for klarna and change type of amount to MinorUnit for OrderDetailsWithAmount (#4979)

- **Commit:** `2807622b`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-10-25T18:29:44+05:30
- **Changes:** 21 files (+122/-95)

## 1109. feat(authz): Make info APIs support `ParentGroup` (#6440)

- **Commit:** `7dcffccf`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-10-30T12:58:41+05:30
- **Changes:** 13 files (+364/-52)

## 1110. refactor(connnector): Structure connector enums in separate files for improved team ownership (#6459)

- **Commit:** `bb246e27`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-10-30T12:58:58+05:30
- **Changes:** 10 files (+13002/-12987)

## 1111. feat(router): Add payments get-intent API for v2 (#6396)

- **Commit:** `c5146085`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2024-10-30T21:26:23+05:30
- **Changes:** 18 files (+570/-195)

## 1112. feat(connector): [Paybox] Add mandates Flow for Paybox (#6378)

- **Commit:** `37513e0f`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-10-30T21:32:59+05:30
- **Changes:** 55 files (+729/-153)

## 1113. feat: add macro to generate ToEncryptable trait (#6313)

- **Commit:** `19cf0f74`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2024-11-04T11:24:13+05:30
- **Changes:** 19 files (+949/-738)

## 1114. refactor(connector): [AIRWALLEX, MULTISAFEPAY, RAZORPAY, SHIFT4, WORLDPAY, ZSL] Move connectors from `router` to `hyperswitch_connectors` crate (#6369)

- **Commit:** `72ee4340`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2024-11-04T20:20:39+05:30
- **Changes:** 28 files (+2389/-2420)

## 1115. feat(db): implement `MerchantAccountInteraface` for `Mockdb` (#6283)

- **Commit:** `5f493a51`
- **Author:** Akhil <akhilgodvsdemon@gmail.com>
- **Date:** 2024-11-05T13:09:46+05:30
- **Changes:** 4 files (+279/-46)

## 1116. Feat(connector): [ELAVON] Template PR (#6309)

- **Commit:** `b481e5cb`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2024-11-05T14:53:31+05:30
- **Changes:** 23 files (+1314/-15)

## 1117. feat(connector): [Paypal] implement vaulting for paypal wallet and cards while purchasing (#5323)

- **Commit:** `22ba2dbb`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-11-05T14:57:43+05:30
- **Changes:** 4 files (+361/-62)

## 1118. Feat(connector): [JP MORGAN] Added Template code for cards integration (#6467)

- **Commit:** `b048e39b`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2024-11-05T20:46:26+05:30
- **Changes:** 25 files (+1316/-12)

## 1119. feat(analytics): implement currency conversion to power multi-currency aggregation (#6418)

- **Commit:** `01c5216f`
- **Author:** Uzair Khan <uzairkhanuk3215@gmail.com>
- **Date:** 2024-11-06T14:46:16+05:30
- **Changes:** 18 files (+273/-24)

## 1120. chore: change serde value to strict type in payment intent domain and diesel model (#6393)

- **Commit:** `a5ac69d1`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-11-08T12:48:01+05:30
- **Changes:** 46 files (+1030/-263)

## 1121. feat(opensearch): refactor global search querybuilder and add case insensitivity opensearch filters (#6476)

- **Commit:** `529f1a76`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-11-08T15:35:24+05:30
- **Changes:** 2 files (+151/-84)

## 1122. Feat(connector): [AMAZON PAY] Added Template code (#6486)

- **Commit:** `fe4931a3`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2024-11-08T15:40:45+05:30
- **Changes:** 25 files (+1322/-21)

## 1123. Refactor(core): interpolate success_based_routing config params with their specific values (#6448)

- **Commit:** `d9ce42fd`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-11-08T17:29:44+05:30
- **Changes:** 8 files (+188/-46)

## 1124. refactor(router): Remove card exp validation for migration api (#6460)

- **Commit:** `1dfcaabf`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2024-11-08T17:43:03+05:30
- **Changes:** 2 files (+400/-3)

## 1125. fix(connector): [Novalnet] Add mandatory fields for wallets and card in config (#6463)

- **Commit:** `3d9f4432`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-11-08T17:56:08+05:30
- **Changes:** 1 files (+347/-2)

## 1126. feat(connector): [worldpay] add support for mandates (#6479)

- **Commit:** `378ec44d`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-11-08T18:00:39+05:30
- **Changes:** 9 files (+549/-119)

## 1127. fix(connector): [fiuu]fix mandates for fiuu (#6487)

- **Commit:** `bc92a2e9`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-11-08T18:23:58+05:30
- **Changes:** 7 files (+259/-73)

## 1128. refactor(payment_methods): refactor customer payment methods list v2 code to follow better code practices (#6433)

- **Commit:** `0389ae74`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-11-08T19:20:14+05:30
- **Changes:** 33 files (+501/-411)

## 1129. feat(router): add `start_redirection` api for three_ds flow in v2 (#6470)

- **Commit:** `6f24bb4e`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-11-08T19:20:25+05:30
- **Changes:** 19 files (+316/-28)

## 1130. feat(analytics): revert remove additional filters from PaymentIntentFilters (#6492)

- **Commit:** `ce95b653`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-11-08T21:03:57+05:30
- **Changes:** 20 files (+370/-2)

## 1131. feat(payment_v2): implement payments sync  (#6464)

- **Commit:** `42bdf47f`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-11-11T18:44:15+05:30
- **Changes:** 65 files (+2453/-496)

## 1132. feat(connector): [NOMUPAY] Add template code (#6382)

- **Commit:** `20a3a1c2`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2024-11-12T12:27:52+05:30
- **Changes:** 25 files (+1304/-9)

## 1133. feat(users): add global support in user roles (#6458)

- **Commit:** `98b141c6`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-11-13T12:21:03+05:30
- **Changes:** 18 files (+211/-34)

## 1134. fix(webhooks): add support for updating mandate details in webhooks flow  (#6523)

- **Commit:** `6eb72e92`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2024-11-13T15:12:58+05:30
- **Changes:** 9 files (+400/-36)

## 1135. feat(openapi): add payment get to openapi  (#6539)

- **Commit:** `600cf446`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-11-13T15:23:40+05:30
- **Changes:** 14 files (+540/-94)

## 1136. feat(core): add Mobile Payment (Direct Carrier Billing) as a payment method (#6196)

- **Commit:** `d0a041c3`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2024-11-14T01:19:59+05:30
- **Changes:** 94 files (+1058/-257)

## 1137. feat(analytics): add `sessionized_metrics` and `currency_conversion` for refunds analytics  (#6419)

- **Commit:** `afd7f7d2`
- **Author:** Uzair Khan <uzair.khan@juspay.in>
- **Date:** 2024-11-14T14:09:30+05:30
- **Changes:** 17 files (+634/-34)

## 1138. feat(themes): Setup themes table (#6533)

- **Commit:** `29be1d4f`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-11-14T14:10:20+05:30
- **Changes:** 15 files (+471/-3)

## 1139. feat(payments_v2): add finish redirection endpoint (#6549)

- **Commit:** `0805a937`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-11-15T14:06:48+05:30
- **Changes:** 29 files (+534/-136)

## 1140. feat(router): add payment incoming webhooks support for v2 (#6551)

- **Commit:** `8e9c3ec8`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-11-19T13:13:58+05:30
- **Changes:** 25 files (+1271/-9)

## 1141. refactor(payment_methods_v2): rename `payment_method` and `payment_method_type` fields and use concrete type for `payment_method_data` (#6555)

- **Commit:** `11e92413`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-11-19T20:33:30+05:30
- **Changes:** 31 files (+1169/-496)

## 1142. feat(connector): [Novalnet] Add minimal customer data feature  (#6570)

- **Commit:** `9787a2be`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-11-20T01:00:49+05:30
- **Changes:** 2 files (+25/-263)

## 1143. feat(routing): add invalidate window as a service for SR based routing (#6264)

- **Commit:** `607b3df3`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-11-20T01:49:09+05:30
- **Changes:** 6 files (+170/-103)

## 1144. feat(router): Add support for network token migration (#6300)

- **Commit:** `012e352d`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2024-11-20T18:43:12+05:30
- **Changes:** 7 files (+487/-47)

## 1145. feat(email): Add SMTP support to allow mails through self hosted/custom SMTP server (#6617)

- **Commit:** `0f563b06`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2024-11-20T19:14:03+05:30
- **Changes:** 11 files (+670/-36)

## 1146. feat(connector): [Xendit] Template PR (#6593)

- **Commit:** `9bc363f1`
- **Author:** AmeyWale-HS <amey.wale@juspay.in>
- **Date:** 2024-11-21T23:35:31+05:30
- **Changes:** 24 files (+1274/-3)

## 1147. feat(connector): [Paypal] implement vaulting for paypal cards via zero mandates (#5324)

- **Commit:** `83e8bc07`
- **Author:** Kiran Kumar <60121719+KiranKBR@users.noreply.github.com>
- **Date:** 2024-11-25T12:29:51+05:30
- **Changes:** 3 files (+260/-31)

## 1148. feat(connector): [Elavon] Implement cards Flow (#6485)

- **Commit:** `68876811`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-11-25T19:42:51+05:30
- **Changes:** 30 files (+1498/-235)

## 1149. feat(connector): [INESPAY] add Connector Template Code (#6614)

- **Commit:** `710186f0`
- **Author:** sweta-kumari-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2024-11-26T12:44:44+05:30
- **Changes:** 27 files (+1316/-14)

## 1150. feat(users): Send welcome to community email in magic link signup (#6639)

- **Commit:** `03423a1f`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-11-26T13:46:56+05:30
- **Changes:** 4 files (+350/-5)

## 1151. refactor(payments_v2): use batch encryption for intent create and confirm intent (#6589)

- **Commit:** `108b1603`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-11-26T13:47:12+05:30
- **Changes:** 8 files (+307/-85)

## 1152. refactor(tenant): use tenant id type (#6643)

- **Commit:** `c9df7b05`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-11-26T13:47:58+05:30
- **Changes:** 32 files (+252/-118)

## 1153. feat(analytics): add `sessionized_metrics` for disputes analytics (#6573)

- **Commit:** `8fbb7663`
- **Author:** Uzair Khan <uzair.khan@juspay.in>
- **Date:** 2024-11-26T18:54:42+05:30
- **Changes:** 13 files (+447/-23)

## 1154. feat: Added grpc based health check (#6441)

- **Commit:** `e922f96c`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-11-26T18:54:55+05:30
- **Changes:** 13 files (+285/-17)

## 1155. fix(analytics): fix bugs in payments page metrics in Analytics V2 dashboard (#6654)

- **Commit:** `93459fde`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-11-28T15:29:55+05:30
- **Changes:** 6 files (+80/-121)

## 1156. feat: add support for sdk session call in v2 (#6502)

- **Commit:** `707f48ce`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2024-11-28T15:31:57+05:30
- **Changes:** 18 files (+1029/-61)

## 1157. feat(connector): worldpay - add dynamic fields and update terminal status mapping (#6468)

- **Commit:** `5a98ed65`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-11-28T19:53:20+05:30
- **Changes:** 17 files (+564/-176)

## 1158. feat(connector): [REDSYS] add Connector Template Code (#6659)

- **Commit:** `19cbcdd9`
- **Author:** sweta-kumari-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2024-11-29T15:34:11+05:30
- **Changes:** 25 files (+1302/-7)

## 1159. feat(users): add tenant id reads in user roles (#6661)

- **Commit:** `9212f776`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-11-29T15:39:55+05:30
- **Changes:** 9 files (+340/-126)

## 1160. fix(openapi): Standardise API naming scheme for V2 (#6510)

- **Commit:** `96393ff3`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2024-11-29T15:58:59+05:30
- **Changes:** 50 files (+872/-167)

## 1161. feat(payment_methods_v2): implement a barebones version of list customer payment methods v2 (#6649)

- **Commit:** `797a0db7`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-12-02T15:29:28+05:30
- **Changes:** 15 files (+173/-187)

## 1162. chore: address Rust 1.83.0 clippy lints and enable more clippy lints (#6705)

- **Commit:** `9a59d0a5`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-12-02T20:00:44+05:30
- **Changes:** 139 files (+147/-417)

## 1163. feat(routing): elimination routing switch for toggling the feature (#6568)

- **Commit:** `f6dde13d`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-12-02T20:13:37+05:30
- **Changes:** 13 files (+682/-268)

## 1164. feat: add resources and granular permission groups for reconciliation (#6591)

- **Commit:** `fa21ef89`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-12-04T14:58:10+05:30
- **Changes:** 18 files (+442/-172)

## 1165. refactor(address): change address to domain address in application (#6608)

- **Commit:** `938b2a89`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-12-04T15:02:43+05:30
- **Changes:** 69 files (+412/-236)

## 1166. feat(themes): Create APIs for managing themes (#6658)

- **Commit:** `3a3e93cb`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-12-04T15:04:13+05:30
- **Changes:** 26 files (+946/-52)

## 1167. refactor(connector): Move connectors Bamboraapac, Boku, Gocardless,  Prophetpay, Rapyd (#6652)

- **Commit:** `36388d45`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2024-12-05T12:52:57+05:30
- **Changes:** 21 files (+1547/-1669)

## 1168. feat(connector): [Nexixpay] add mandates flow for cards (#6259)

- **Commit:** `62521f36`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2024-12-05T14:16:04+05:30
- **Changes:** 5 files (+974/-143)

## 1169. feat(routing): Enable volume split for dynamic routing (#6662)

- **Commit:** `03b936a1`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-12-05T14:38:23+05:30
- **Changes:** 12 files (+302/-75)

## 1170. feat(analytics): Add refund sessionized metrics for Analytics V2 dashboard (#6616)

- **Commit:** `774a53ee`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2024-12-05T15:39:40+05:30
- **Changes:** 29 files (+1527/-78)

## 1171. feat(webhooks): adyen - consume and update connector's network_transaction_id in payment_methods (#6738)

- **Commit:** `871a3637`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-12-05T17:23:44+05:30
- **Changes:** 7 files (+191/-87)

## 1172. feat(connector): Added a new CaptureMethod SequentialAutomatic to Support CIT Mandates for Paybox (#6587)

- **Commit:** `e5dde6ac`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2024-12-05T18:50:15+05:30
- **Changes:** 88 files (+761/-130)

## 1173. chore: enable `clippy::trivially_copy_pass_by_ref` lint and address it (#6724)

- **Commit:** `d17d2fe0`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-12-05T20:11:40+05:30
- **Changes:** 154 files (+423/-429)

## 1174. feat(users): add support for tenant level users (#6708)

- **Commit:** `357e8a00`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2024-12-06T17:31:55+05:30
- **Changes:** 22 files (+701/-128)

## 1175. feat(dynamic_routing): analytics improvement using separate postgres table (#6723)

- **Commit:** `5918014d`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-12-07T14:35:44+05:30
- **Changes:** 16 files (+256/-12)

## 1176. feat(core): Add payments update-intent API for v2 (#6490)

- **Commit:** `19f810ae`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2024-12-09T12:50:07+05:30
- **Changes:** 23 files (+1445/-511)

## 1177. feat(connector): [Unifiedauthenticationservice] add Connector Template Code (#6732)

- **Commit:** `8777f415`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2024-12-10T16:06:23+05:30
- **Changes:** 25 files (+1360/-6)

## 1178. build(deps): bump opentelemetry crates to 0.27 (#6774)

- **Commit:** `47a3d2b2`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-12-10T16:35:34+05:30
- **Changes:** 86 files (+737/-1084)

## 1179. refactor(users): remove lineage checks in roles get operations (#6701)

- **Commit:** `f96a87d0`
- **Author:** Riddhiagrawal001 <50551695+Riddhiagrawal001@users.noreply.github.com>
- **Date:** 2024-12-10T16:49:17+05:30
- **Changes:** 15 files (+188/-149)

## 1180. feat(core): Add uas framework support (#6743)

- **Commit:** `9466ced8`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-12-11T17:32:42+05:30
- **Changes:** 55 files (+1284/-94)

## 1181. refactor(connector): Move connectors Datatrans, Paybox, Placetopay, Bluesnap  from router crate to hyperswitch_connector crate (#6730)

- **Commit:** `da5c34a3`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2024-12-12T12:48:05+05:30
- **Changes:** 21 files (+1628/-1584)

## 1182. feat(connector): [DEUTSCHEBANK, FIUU ] Handle 2xx errors given by Connector (#6727)

- **Commit:** `573fc2ce`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2024-12-12T15:04:37+05:30
- **Changes:** 2 files (+211/-103)

## 1183. feat(core): payment links - add support for custom background image and layout in details section (#6725)

- **Commit:** `d11d8740`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2024-12-12T20:50:33+05:30
- **Changes:** 19 files (+775/-87)

## 1184. feat(routing): build the gRPC interface for communicating with the external service to perform elimination routing (#6672)

- **Commit:** `2a66f4a3`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2024-12-13T10:45:08+05:30
- **Changes:** 9 files (+473/-210)

## 1185. refactor(core): structure of split payments (#6706)

- **Commit:** `5a85213e`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2024-12-13T15:26:15+05:30
- **Changes:** 46 files (+828/-519)

## 1186. feat(router): add `click_to_pay` block in payments sessions response if enabled (#6829)

- **Commit:** `5aa8ea03`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2024-12-13T16:07:33+05:30
- **Changes:** 8 files (+261/-0)

## 1187. feat(users): Incorporate themes in user APIs (#6772)

- **Commit:** `4b989fe0`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-12-16T14:23:31+05:30
- **Changes:** 27 files (+687/-89)

## 1188. feat(core): Add click to pay support in hyperswitch (#6769)

- **Commit:** `165ead61`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2024-12-16T19:15:32+05:30
- **Changes:** 50 files (+1287/-855)

## 1189. feat(analytics): Analytics Request Validator and config driven forex feature (#6733)

- **Commit:** `c883aa59`
- **Author:** Uzair Khan <uzair.khan@juspay.in>
- **Date:** 2024-12-17T15:53:00+05:30
- **Changes:** 16 files (+429/-161)

## 1190. refactor(customers_v2): address panics and some bugs in customers v2 endpoints (#6836)

- **Commit:** `dfbfce4e`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2024-12-17T15:54:27+05:30
- **Changes:** 56 files (+906/-475)

## 1191. refactor(dynamic_routing): update the authentication for update config to include JWT type (#6785)

- **Commit:** `db51ec43`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2024-12-18T14:28:11+05:30
- **Changes:** 4 files (+282/-5)

## 1192. FEAT(klarna): Klarna Kustom Checkout Integration (#6839)

- **Commit:** `c525c9f4`
- **Author:** sweta-kumari-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2024-12-19T13:11:44+05:30
- **Changes:** 29 files (+593/-265)

## 1193. feat(payment_methods): add support to pass apple pay recurring details to obtain apple pay merchant token (#6770)

- **Commit:** `60742499`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-12-19T18:33:09+05:30
- **Changes:** 14 files (+748/-3)

## 1194. feat(router): add /relay endpoint (#6870)

- **Commit:** `22de8ad1`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-12-20T19:36:54+05:30
- **Changes:** 11 files (+468/-1)

## 1195. feat(payments_v2): implement payments capture v2 (#6722)

- **Commit:** `977cb704`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-12-20T20:54:57+05:30
- **Changes:** 22 files (+1925/-287)

## 1196. feat(router): add db interface for `/relay` (#6879)

- **Commit:** `0f8b0b3b`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-12-22T22:41:28+05:30
- **Changes:** 29 files (+1152/-58)

## 1197. feat(payment_methods_v2): Added Ephemeral auth for v2 (#6813)

- **Commit:** `24401bc1`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2024-12-22T23:04:45+05:30
- **Changes:** 23 files (+688/-126)

## 1198. feat(connector): [JPMORGAN] add Payment flows for cards (#6668)

- **Commit:** `adcddd64`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2024-12-22T23:13:11+05:30
- **Changes:** 25 files (+1341/-187)

## 1199. feat(payments_v2): add payment method list endpoint (#6805)

- **Commit:** `d4b3dbc1`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2024-12-23T15:37:16+05:30
- **Changes:** 45 files (+1314/-728)

## 1200. feat(core): implemented platform merchant account (#6882)

- **Commit:** `95fcf2a4`
- **Author:** Rachit Naithani <81706961+racnan@users.noreply.github.com>
- **Date:** 2024-12-23T18:23:22+05:30
- **Changes:** 64 files (+595/-16)

## 1201. feat(router): add /retrieve api for relay (#6918)

- **Commit:** `04787313`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2024-12-23T18:23:55+05:30
- **Changes:** 9 files (+269/-9)

## 1202. feat(router): add endpoint for listing connector features  (#6612)

- **Commit:** `a423ff53`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2024-12-24T14:37:19+05:30
- **Changes:** 124 files (+1490/-252)

## 1203. feat(users): Add email domain based restriction for dashboard entry APIs (#6940)

- **Commit:** `227c274e`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2024-12-30T12:39:16+05:30
- **Changes:** 14 files (+322/-52)

## 1204. feat(core): add columns unified error code and error message in refund table (#6933)

- **Commit:** `c4d36b50`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2025-01-07T13:01:17+05:30
- **Changes:** 30 files (+237/-166)

## 1205. feat(users): handle edge features for users in tenancy (#6990)

- **Commit:** `d04e840c`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2025-01-08T14:37:02+05:30
- **Changes:** 18 files (+556/-140)

## 1206. fix(dummyconnector): add tenant id in dummyconnector requests (#7008)

- **Commit:** `9c983b68`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2025-01-09T14:41:38+05:30
- **Changes:** 28 files (+194/-51)

## 1207. feat(router): add support for relay refund incoming webhooks (#6974)

- **Commit:** `d850f17b`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-01-10T13:08:36+05:30
- **Changes:** 16 files (+485/-94)

## 1208. feat(connector): [Novalnet] Add zero auth mandate (#6631)

- **Commit:** `7b306a90`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2025-01-10T14:46:37+05:30
- **Changes:** 10 files (+473/-27)

## 1209. feat(payment_methods_v2): add payment methods list endpoint (#6938)

- **Commit:** `6a1f5a88`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2025-01-13T15:07:19+05:30
- **Changes:** 47 files (+1218/-854)

## 1210. feat(connector): [Deutschebank] Implement Card 3ds (#6844)

- **Commit:** `ac753352`
- **Author:** Debarshi Gupta <debarshigupta47@gmail.com>
- **Date:** 2025-01-13T16:49:50+05:30
- **Changes:** 8 files (+990/-111)

## 1211. feat(core): diesel models, domain models and db interface changes for callback_mapper table (#6571)

- **Commit:** `043cf8e0`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-01-15T15:26:14+05:30
- **Changes:** 18 files (+219/-13)

## 1212. feat(connector): [Xendit] ADD Cards & Mandates Flow  (#6966)

- **Commit:** `bbf88446`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-01-15T15:37:30+05:30
- **Changes:** 21 files (+1534/-210)

## 1213. refactor(proxy): specify hosts for proxy exclusion instead of complete URLs (#6957)

- **Commit:** `bd1f0770`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2025-01-15T17:39:37+05:30
- **Changes:** 10 files (+58/-167)

## 1214. chore: address Rust 1.84.0 clippy lints (#7021)

- **Commit:** `4664d4bc`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2025-01-15T18:19:41+05:30
- **Changes:** 36 files (+159/-213)

## 1215. refactor(router): refactor ctp flow to fetch mca_id and get the connector creds instead of connector_name (#6859)

- **Commit:** `e9fcfc45`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-01-20T17:32:05+05:30
- **Changes:** 16 files (+242/-152)

## 1216. feat(connectors): fiuu,novalnet,worldpay - extend NTI flows (#6946)

- **Commit:** `d6b06605`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-01-21T12:49:48+05:30
- **Changes:** 19 files (+605/-172)

## 1217. feat(router): add payment method-specific features to connector feature list (#6963)

- **Commit:** `e35f7079`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-01-21T13:33:09+05:30
- **Changes:** 10 files (+229/-93)

## 1218. feat(routing): Integrate global success rates (#6950)

- **Commit:** `39d2d6c4`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-01-21T17:14:14+05:30
- **Changes:** 11 files (+196/-17)

## 1219. refactor: [CYBERSOURCE, BANKOFAMERICA, WELLSFARGO] Move code to crate hyperswitch_connectors (#6908)

- **Commit:** `be018963`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-01-22T23:21:19+05:30
- **Changes:** 19 files (+3070/-3068)

## 1220. refactor(currency_conversion): re frame the currency_conversion crate to make api calls on background thread (#6906)

- **Commit:** `858866f9`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-01-28T23:27:23+05:30
- **Changes:** 9 files (+142/-203)

## 1221. fix(multitenancy): add a fallback for get commands in redis (#7043)

- **Commit:** `57072976`
- **Author:** Kartikeya Hegde <karthikey.hegde@juspay.in>
- **Date:** 2025-01-29T00:38:17+05:30
- **Changes:** 34 files (+362/-204)

## 1222. feat(connector): add template code for chargebee (#7036)

- **Commit:** `ad5491f1`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-01-29T16:03:21+05:30
- **Changes:** 24 files (+1313/-14)

## 1223. feat(router): add core changes for external authentication flow through unified_authentication_service (#7063)

- **Commit:** `ae39374c`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-02-04T01:10:24+05:30
- **Changes:** 20 files (+1190/-261)

## 1224. feat(core): google pay decrypt flow (#6991)

- **Commit:** `e0ec27d9`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-02-05T15:24:57+05:30
- **Changes:** 39 files (+1158/-27)

## 1225. feat(users): custom role at profile read (#6875)

- **Commit:** `899c207d`
- **Author:** Riddhiagrawal001 <50551695+Riddhiagrawal001@users.noreply.github.com>
- **Date:** 2025-02-05T19:02:38+05:30
- **Changes:** 19 files (+481/-273)

## 1226. refactor(core): add recurring customer support for nomupay payouts. (#6687)

- **Commit:** `8d8ebe90`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2025-02-05T19:03:11+05:30
- **Changes:** 25 files (+1355/-238)

## 1227. feat(payments_v2): implement create and confirm intent flow (#7106)

- **Commit:** `67ea754e`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2025-02-05T19:07:11+05:30
- **Changes:** 34 files (+1866/-1322)

## 1228. feat(core): Implement 3ds decision manger for V2 (#7022)

- **Commit:** `19009597`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-02-05T19:07:46+05:30
- **Changes:** 22 files (+362/-153)

## 1229. feat(connector): [INESPAY] Integrate Sepa Bank Debit (#6755)

- **Commit:** `ce2485c3`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-02-05T19:11:41+05:30
- **Changes:** 10 files (+574/-160)

## 1230. refactor(router): store `network_transaction_id` for `off_session` payments irrespective of the `is_connector_agnostic_mit_enabled` config (#7083)

- **Commit:** `f9a4713a`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-02-06T15:57:34+05:30
- **Changes:** 3 files (+385/-25)

## 1231. feat(connector): [COINGATE] Add Template PR  (#7052)

- **Commit:** `dddb1b06`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-02-06T19:13:36+05:30
- **Changes:** 21 files (+1323/-27)

## 1232. feat(routing): Contract based routing integration  (#6761)

- **Commit:** `60ddddf2`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-02-06T19:16:00+05:30
- **Changes:** 23 files (+1968/-210)

## 1233. feat(core): Add support for v2 payments get intent using merchant reference id (#7123)

- **Commit:** `e17ffd12`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-02-06T19:16:36+05:30
- **Changes:** 10 files (+245/-1)

## 1234. feat(connector): [DataTrans] ADD 3DS Flow (#6026)

- **Commit:** `4693d21b`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-02-07T10:19:40+05:30
- **Changes:** 13 files (+383/-62)

## 1235. refactor(connector): Move connectors Aci, Braintree, Globalpay, Iatapay, Itaubank, Klarna, Mifinity and Nuvei from router to hyperswitch_connectors crate (#7167)

- **Commit:** `7dfe4004`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2025-02-07T15:18:24+05:30
- **Changes:** 31 files (+3339/-3465)

## 1236. feat(opensearch): add amount and customer_id as filters and handle name for different indexes (#7073)

- **Commit:** `df328c5e`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-02-07T17:10:12+05:30
- **Changes:** 3 files (+162/-65)

## 1237. feat(router): add adyen split payments support (#6952)

- **Commit:** `323d7630`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-02-10T11:56:39+05:30
- **Changes:** 119 files (+1387/-666)

## 1238. refactor(router): add feature_metadata for merchant_connector_account create v2 flow (#7144)

- **Commit:** `647e1631`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-02-10T16:51:07+05:30
- **Changes:** 14 files (+356/-10)

## 1239. refactor(core): add support for expand attempt list in psync v2 (#7209)

- **Commit:** `d0933170`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-02-11T16:13:51+05:30
- **Changes:** 15 files (+407/-65)

## 1240. feat(payment_methods_session_v2): add payment methods session endpoints (#7107)

- **Commit:** `96153824`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2025-02-11T16:59:58+05:30
- **Changes:** 57 files (+2671/-1431)

## 1241. feat(connector): [GETNET] add Connector Template Code (#7105)

- **Commit:** `60310b48`
- **Author:** sweta-kumari-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-02-11T22:40:38+05:30
- **Changes:** 26 files (+1324/-13)

## 1242. refactor(schema): add a new column for storing large connector transaction IDs (#7017)

- **Commit:** `fa09db15`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-02-12T13:18:38+05:30
- **Changes:** 28 files (+987/-122)

## 1243. feat(core): 3ds decision manager for v2 (#7089)

- **Commit:** `52ae92bc`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-02-12T18:11:29+05:30
- **Changes:** 14 files (+244/-26)

## 1244. feat(core): add support to generate session token response from both `connector_wallets_details` and `metadata` (#7140)

- **Commit:** `66d9c731`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-02-13T13:10:28+05:30
- **Changes:** 11 files (+297/-163)

## 1245. feat(connector): [Moneris] add template code (#7216)

- **Commit:** `b09905ec`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-02-13T15:13:12+05:30
- **Changes:** 24 files (+1308/-8)

## 1246. refactor(payments_v2): create customer at connector end and populate connector customer ID (#7246)

- **Commit:** `17f9e6ee`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2025-02-14T14:58:54+05:30
- **Changes:** 11 files (+356/-114)

## 1247. refactor(router):  add revenue_recovery_metadata to payment intent in diesel and api model for v2 flow (#7176)

- **Commit:** `2ee22cdf`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-02-14T16:19:58+05:30
- **Changes:** 6 files (+285/-3)

## 1248. feat(connector): [Datatrans] add mandate flow (#7245)

- **Commit:** `e2043dee`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-02-14T18:10:25+05:30
- **Changes:** 3 files (+370/-48)

## 1249. feat(payment_methods_v2): add support for network tokenization (#7145)

- **Commit:** `0b972e38`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-02-14T18:10:42+05:30
- **Changes:** 21 files (+1147/-177)

## 1250. feat(core): introduce accounts schema for accounts related tables (#7113)

- **Commit:** `0ba4ccfc`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-02-14T18:11:06+05:30
- **Changes:** 26 files (+308/-56)

## 1251. feat(utils): add iso representation for each state for european countries (#7273)

- **Commit:** `c337be66`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-02-15T20:39:26+05:30
- **Changes:** 6 files (+4791/-4)

## 1252. feat(coingate): Add Crypto Pay Flow (#7247)

- **Commit:** `c868ff38`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-02-17T15:10:11+05:30
- **Changes:** 19 files (+178/-373)

## 1253. refactor(utils): use to_state_code of hyperswitch_connectors in router (#7278)

- **Commit:** `b97370d5`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-02-17T18:22:32+05:30
- **Changes:** 6 files (+1062/-42)

## 1254. feat(core): api ,domain and diesel model changes for extended authorization (#6607)

- **Commit:** `e14d6c44`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-02-18T19:42:19+05:30
- **Changes:** 31 files (+535/-60)

## 1255. feat(connector): [Moneris] Add payments flow (#7249)

- **Commit:** `d18d98a1`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-02-18T19:46:51+05:30
- **Changes:** 18 files (+1094/-111)

## 1256. feat(core): add hypersense integration api  (#7218)

- **Commit:** `22633be5`
- **Author:** Uzair Khan <uzair.khan@juspay.in>
- **Date:** 2025-02-19T13:23:26+05:30
- **Changes:** 14 files (+326/-6)

## 1257. refactor(utils): match string for state with SDK's naming convention (#7300)

- **Commit:** `f3ca2009`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-02-19T16:30:14+05:30
- **Changes:** 2 files (+2879/-2255)

## 1258. feat(core): add support for confirmation flow for click to pay (#6982)

- **Commit:** `74bbf4bf`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-02-20T12:47:29+05:30
- **Changes:** 25 files (+906/-287)

## 1259. feat(router): Add Payments - List endpoint for v2 (#7191)

- **Commit:** `d1f537e2`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-02-20T16:39:38+05:30
- **Changes:** 20 files (+1816/-91)

## 1260. feat(router): [Xendit] add support for split payments (#7143)

- **Commit:** `451acba0`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-02-20T19:29:35+05:30
- **Changes:** 24 files (+1142/-32)

## 1261. fix(routing): Fixed 5xx error logs in dynamic routing metrics (#7335)

- **Commit:** `049fcdb3`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-02-21T23:14:11+05:30
- **Changes:** 1 files (+378/-361)

## 1262. feat(connector): Add support for passive churn recovery webhooks (#7109)

- **Commit:** `06889728`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-02-23T02:28:10+05:30
- **Changes:** 32 files (+992/-36)

## 1263. feat(core): [Card Testing Guard] Implement Card Testing Guard  (#7108)

- **Commit:** `2451e9b7`
- **Author:** Debarshi Gupta <debarshigupta47@gmail.com>
- **Date:** 2025-02-25T05:18:57+05:30
- **Changes:** 41 files (+1159/-8)

## 1264. feat(connector): [JPMORGAN, PAYU, DIGITALVIRGO, PAYBOX, BITPAY, HELCIM] added in feature matrix api (#7148)

- **Commit:** `c92b9661`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-02-26T00:32:48+05:30
- **Changes:** 12 files (+616/-115)

## 1265. feat(connector): [DLOCAL, MOLLIE, MIFINITY, RAZORPAY, VOLT] add in feature matrix api (#7290)

- **Commit:** `eef1aeb0`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-02-26T01:04:45+05:30
- **Changes:** 12 files (+499/-34)

## 1266. feat(connector): [Nomupay] Implement nomupay payouts flows (#6511)

- **Commit:** `501365c8`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2025-02-26T01:06:27+05:30
- **Changes:** 30 files (+1406/-751)

## 1267. fix(connector): Ideal and multiple other failing PMs fixed in Ayden (#7139)

- **Commit:** `e704d175`
- **Author:** sweta-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-02-26T01:07:16+05:30
- **Changes:** 3 files (+150/-390)

## 1268. feat(payment_method_session): implement payment methods session confirm (#7248)

- **Commit:** `0fb01917`
- **Author:** Narayan Bhat <48803246+Narayanbhat166@users.noreply.github.com>
- **Date:** 2025-02-26T22:54:53+05:30
- **Changes:** 45 files (+2135/-931)

## 1269. refactor(v1v2): refactor database queries for v1 and v2 (#7244)

- **Commit:** `65cfaaec`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-02-27T12:24:37+05:30
- **Changes:** 48 files (+619/-479)

## 1270. feat(connector): [PAYSTACK] Template PR (#7285)

- **Commit:** `5965d0f8`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-02-27T13:33:01+05:30
- **Changes:** 28 files (+1328/-11)

## 1271. feat(connector): Add support for chargebee recovery webhooks (#7110)

- **Commit:** `37aacfa1`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-02-27T17:02:18+05:30
- **Changes:** 16 files (+436/-14)

## 1272. feat(core): create a process_tracker workflow for PCR (#7124)

- **Commit:** `44dc45b8`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2025-02-27T18:29:06+05:30
- **Changes:** 23 files (+855/-32)

## 1273. refactor(relay): add trait based implementation for relay (#7264)

- **Commit:** `cdfbb82f`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-03-03T12:22:27+05:30
- **Changes:** 7 files (+261/-118)

## 1274. feat(connector): introduce `feature_matrix` api to coinbase, iatapay, nexixpay and square (#7339)

- **Commit:** `c56f5719`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-03-03T12:33:50+05:30
- **Changes:** 11 files (+526/-111)

## 1275. feat(router): Add support for retries with clear pan and network token payment method data (#6905)

- **Commit:** `44eec7a9`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-03-03T13:19:58+05:30
- **Changes:** 45 files (+722/-261)

## 1276. feat(connector): add template code for stripebilling (#7228)

- **Commit:** `af8778e0`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-03-03T15:04:51+05:30
- **Changes:** 24 files (+1321/-5)

## 1277. refactor(connector): [AUTHORIZEDOTNET,CHECKOUT,NOON,OPAYO,OPENNODE,PAYME,TRUSTPAY] Move to crate hyperswitch_connectors (#7235)

- **Commit:** `241653bd`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2025-03-04T11:55:43+05:30
- **Changes:** 22 files (+3191/-3407)

## 1278. feat(xendit): Add Payment Webhooks  (#7277)

- **Commit:** `6553e29e`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-03-04T13:24:02+05:30
- **Changes:** 5 files (+192/-80)

## 1279. feat(core): Add support for cards bin update (#7194)

- **Commit:** `8e922d30`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2025-03-04T13:55:29+05:30
- **Changes:** 12 files (+629/-17)

## 1280. feat(router): add proxy-confirm-intent api for payments in v2 flow (#7215)

- **Commit:** `30f321bc`
- **Author:** Aditya Chaurasia <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-03-05T13:31:21+05:30
- **Changes:** 26 files (+1246/-97)

## 1281. feat(connector): add template code for recurly (#7284)

- **Commit:** `a1691d1b`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-03-05T14:52:09+05:30
- **Changes:** 24 files (+1311/-10)

## 1282. fix(connector): [Braintree] Consume merchant_account_id and merchant_config_currency in payment requests (#7408)

- **Commit:** `00d69bd9`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2025-03-05T16:30:28+05:30
- **Changes:** 16 files (+229/-11)

## 1283. feat(payment_link): expose payment link configs for SDK UI rules and payment button (#7427)

- **Commit:** `6a5ce266`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-03-05T22:09:37+05:30
- **Changes:** 16 files (+199/-21)

## 1284. feat(core): add additional revenue recovery call flow (#7402)

- **Commit:** `9e4135cd`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-03-06T12:10:34+05:30
- **Changes:** 23 files (+309/-20)

## 1285. feat(connector): Added ThreeDs server integration template pr (#7424)

- **Commit:** `7e5da488`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-03-06T15:45:08+05:30
- **Changes:** 29 files (+1509/-20)

## 1286. feat(analytics): refactor and rewrite authentication related analytics (#7433)

- **Commit:** `1ff273e1`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-03-06T16:31:31+05:30
- **Changes:** 18 files (+198/-193)

## 1287. feat(router): add capability to force challenge for 3DS Payments through Netcetera and send few optional fields (#7429)

- **Commit:** `957a2285`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-03-06T18:32:27+05:30
- **Changes:** 17 files (+195/-70)

## 1288. feat(analytics): add new filters, dimensions and metrics for authentication analytics (#7451)

- **Commit:** `7473182b`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-03-06T21:49:44+05:30
- **Changes:** 27 files (+1177/-81)

## 1289. feat(hipay): Add Template PR (#7360)

- **Commit:** `add51526`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-03-07T12:43:27+05:30
- **Changes:** 25 files (+1327/-20)

## 1290. feat(core): add bulk tokenization flows (#7066)

- **Commit:** `2ff0d4f9`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-03-07T18:20:18+05:30
- **Changes:** 26 files (+2742/-38)

## 1291. feat(core): Add record attempt operation for revenue recovery webhooks (#7236)

- **Commit:** `24aa0034`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-03-07T19:34:47+05:30
- **Changes:** 18 files (+1024/-63)

## 1292. Feat(connector): Rapyd, Bamboraapac, Gocardless, Powertranz, Shift4 and Worldline added in feature matrix (#7136)

- **Commit:** `9fe9e9e0`
- **Author:** Suman Maji <77887221+sumanmaji4@users.noreply.github.com>
- **Date:** 2025-03-11T16:21:14+05:30
- **Changes:** 13 files (+828/-126)

## 1293. feat(connector): [BILLWERK, FISERVEMEA, TSYS] add in feature matrix api (#7165)

- **Commit:** `e15c8146`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-03-11T18:47:07+05:30
- **Changes:** 9 files (+344/-62)

## 1294. feat(connector): implement wallet mandates for authorizedotnet (#7412)

- **Commit:** `07733a5c`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-03-11T19:15:57+05:30
- **Changes:** 9 files (+145/-57)

## 1295. refactor(pm): create new crate for payment methods (#7355)

- **Commit:** `a31d1403`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-03-12T03:10:53+05:30
- **Changes:** 32 files (+2076/-2098)

## 1296. feat(analytics): modified authentication queries and added generate report for authentications (#7483)

- **Commit:** `9683b2a8`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-03-12T16:14:09+05:30
- **Changes:** 19 files (+267/-18)

## 1297. feat(connector): Add record back connector integration flow  (#7416)

- **Commit:** `13a27490`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-03-12T17:33:42+05:30
- **Changes:** 13 files (+272/-39)

## 1298. feat(users): Add V2 User APIs to Support Modularity for Merchant Accounts (#7386)

- **Commit:** `d1f53036`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-03-12T19:31:24+05:30
- **Changes:** 12 files (+249/-37)

## 1299. feat(payment_methods_v2): add total-payment-method-count api (#7479)

- **Commit:** `4f6174d1`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-03-13T00:41:12+05:30
- **Changes:** 11 files (+188/-21)

## 1300. feat(core): Add V2 Authentication to all available endpoints (#7487)

- **Commit:** `3667a7ff`
- **Author:** Gaurav Rawat <104276743+GauravRawat369@users.noreply.github.com>
- **Date:** 2025-03-13T01:49:09+05:30
- **Changes:** 9 files (+325/-50)

## 1301. refactor(payment_methods_v2): refactor network tokenization flow for v2 (#7309)

- **Commit:** `bba414cd`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-03-13T02:53:35+05:30
- **Changes:** 16 files (+591/-414)

## 1302. feat(router):  add connector field to PaymentRevenueRecoveryMetadata and implement schedule_failed_payment   (#7462)

- **Commit:** `aa337eee`
- **Author:** Aditya Chaurasia <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-03-13T14:48:36+05:30
- **Changes:** 18 files (+174/-51)

## 1303. refactor(connector): [PAYPAL, ADYEN] Move to crate hyperswitch_connectors (#7431)

- **Commit:** `cf364192`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-03-13T17:13:20+05:30
- **Changes:** 14 files (+2304/-2443)

## 1304. feat(connector): [Hipay] Add Card Payments Flow  (#7475)

- **Commit:** `3e7db573`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-03-13T19:36:40+05:30
- **Changes:** 21 files (+1680/-198)

## 1305. refactor(process_tracker): Integrate proxy_payments api to process tracker workflow (#7480)

- **Commit:** `ba3ad87e`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2025-03-17T10:20:14+05:30
- **Changes:** 9 files (+296/-79)

## 1306. feat(connector): [PAYSTACK] Electronic Fund Transfer(EFT) Payment Flows (#7440)

- **Commit:** `c39ecda7`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-03-17T12:17:47+05:30
- **Changes:** 5 files (+478/-133)

## 1307. feat(connector): [GETNET] Add cards payment flow (#7256)

- **Commit:** `d346d38f`
- **Author:** sweta-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-03-17T19:55:52+05:30
- **Changes:** 25 files (+1860/-131)

## 1308. feat: scheme error code and messages in payments api response (#7528)

- **Commit:** `c702535e`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-03-17T19:59:18+05:30
- **Changes:** 165 files (+1011/-60)

## 1309. feat(connector): [Stripebilling] add incoming webhook support (#7417)

- **Commit:** `32824441`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-03-17T20:10:10+05:30
- **Changes:** 6 files (+282/-7)

## 1310. feat(connector): [Chargebee] Add record back support for chargebee (#7505)

- **Commit:** `e77bb71c`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-03-18T18:12:46+05:30
- **Changes:** 8 files (+494/-56)

## 1311. feat(connector): [Nexixpay] add setup mandate flow (#7532)

- **Commit:** `f6633a72`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2025-03-18T23:11:24+05:30
- **Changes:** 8 files (+364/-127)

## 1312. build(deps): update aws dependencies (#4194)

- **Commit:** `afca5063`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2025-03-19T16:48:46+05:30
- **Changes:** 6 files (+659/-786)

## 1313. chore: update payment method configs for globalpay (#7512)

- **Commit:** `23a2a0cf`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-03-20T12:34:48+05:30
- **Changes:** 11 files (+242/-1)

## 1314. feat(connectors): [Redsys] add 3D secure card payment support, including transaction capture, cancellation, and refunds (#7508)

- **Commit:** `a1ecce8f`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-03-21T15:08:44+05:30
- **Changes:** 58 files (+2995/-378)

## 1315. refactor(dynamic_routing): change insert operation to upsert for dynamic_routing_stats (#7398)

- **Commit:** `68aac34e`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-03-21T17:04:41+05:30
- **Changes:** 5 files (+219/-31)

## 1316. feat: core changes for extended authorization (#6766)

- **Commit:** `c3c4f50f`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-03-21T17:08:02+05:30
- **Changes:** 26 files (+340/-29)

## 1317. refactor(router): make error_type generic in domain_models inorder to avoid conversion of errors in storage_impl (#7537)

- **Commit:** `80218d0f`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-03-21T17:13:19+05:30
- **Changes:** 38 files (+380/-428)

## 1318. feat(webhook): Return events list and total_count on list initial delivery attempt call (#7243)

- **Commit:** `4d57f5e6`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-03-21T17:31:34+05:30
- **Changes:** 9 files (+317/-88)

## 1319. feat(connectors): [Redsys] add Psync and Rsync support (#7586)

- **Commit:** `3f18c944`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-03-22T11:03:33+05:30
- **Changes:** 7 files (+613/-29)

## 1320. feat(connector): [Coingate] implement refunds  (#7513)

- **Commit:** `4af86523`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-03-24T00:02:30+05:30
- **Changes:** 7 files (+325/-25)

## 1321. feat(refunds): Add refunds diesel model support in V2 API (#7503)

- **Commit:** `bc8b9409`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-03-24T16:13:18+05:30
- **Changes:** 24 files (+914/-40)

## 1322. refactor(webhook): add jwt authenticated endpoint to list unique webhook events for a profile (#7325)

- **Commit:** `70107990`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-03-24T16:57:22+05:30
- **Changes:** 6 files (+195/-14)

## 1323. feat(connector): [Recurly] Add record back support for recurly [V2] (#7544)

- **Commit:** `2b70c945`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-03-24T16:57:43+05:30
- **Changes:** 3 files (+197/-3)

## 1324. feat(connector): [TRUSTPAY]  implement Banktransfer PaymentMethod (#7575)

- **Commit:** `dbcca0fb`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-03-25T19:55:01+05:30
- **Changes:** 46 files (+463/-85)

## 1325. feat: add routing support for v2 sdk session flow (#6763)

- **Commit:** `c3e8c67b`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-03-26T13:47:52+05:30
- **Changes:** 65 files (+3358/-3881)

## 1326. feat(core): add profile level config for debit routing feature (#7470)

- **Commit:** `8e854657`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-03-26T19:16:49+05:30
- **Changes:** 13 files (+235/-18)

## 1327. feat(themes): Add email configuration support for themes (#7580)

- **Commit:** `7805a20d`
- **Author:** Kanika Bansal <kanika.bansal@juspay.in>
- **Date:** 2025-03-26T19:17:01+05:30
- **Changes:** 10 files (+596/-764)

## 1328. refactor(connector): [STRIPE] Bank Transfer Api Refactor (#7599)

- **Commit:** `e9433d98`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-03-27T16:47:11+05:30
- **Changes:** 4 files (+183/-409)

## 1329. feat(router): Add payment_methods_session_delete_payment_method endpoint [V2] (#7409)

- **Commit:** `652fae4f`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-03-27T16:49:36+05:30
- **Changes:** 11 files (+214/-10)

## 1330. refactor(connector): [Noon] Implement Paypal Payment Method (#7610)

- **Commit:** `5153e361`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-03-27T16:50:24+05:30
- **Changes:** 11 files (+482/-18)

## 1331. feat(core): Add support for process tracker retrieve api in v2 (#7602)

- **Commit:** `87140bfc`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2025-03-27T16:52:03+05:30
- **Changes:** 33 files (+430/-111)

## 1332. feat(connector): Introduce connector template code for Facilitapay (#7631)

- **Commit:** `f3d6b15a`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-03-27T18:29:50+05:30
- **Changes:** 24 files (+1352/-32)

## 1333. feat(core): Add visa click to pay support (#7562)

- **Commit:** `9e5e6be7`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-03-28T13:23:59+05:30
- **Changes:** 27 files (+168/-92)

## 1334. feat(webhook): Add is_delivered filter to list initial attempts endpoint (#7344)

- **Commit:** `55d27ce1`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-03-28T15:59:31+05:30
- **Changes:** 17 files (+194/-12)

## 1335. feat(wasm): google pay decryption flow changes (#7616)

- **Commit:** `ac4af691`
- **Author:** Susritha <106534816+susrithasabbini@users.noreply.github.com>
- **Date:** 2025-03-28T15:59:49+05:30
- **Changes:** 4 files (+2217/-12)

## 1336. refactor(request_body): Added FRM data in payment request (#7615)

- **Commit:** `b00deb96`
- **Author:** sweta-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-03-28T17:08:55+05:30
- **Changes:** 1 files (+342/-38)

## 1337. feat(core): implement `NameType` for name validation (#6734)

- **Commit:** `1100dcc6`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-04-01T14:58:54+05:30
- **Changes:** 72 files (+734/-364)

## 1338. feat(router): add payment method display name to feature matrix response (#7639)

- **Commit:** `e8afec2f`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-04-01T17:11:15+05:30
- **Changes:** 7 files (+701/-31)

## 1339. feat(payment_methods_v2): single use token implementation (#7485)

- **Commit:** `f7ea4cce`
- **Author:** Shivansh Mathur <104988143+ShivanshMathurJuspay@users.noreply.github.com>
- **Date:** 2025-04-01T17:34:01+05:30
- **Changes:** 10 files (+464/-30)

## 1340. fix(connectors): [Hipay] Fix 3DS Mandatory Fields (#7603)

- **Commit:** `446716ee`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-04-01T23:10:08+05:30
- **Changes:** 13 files (+331/-58)

## 1341. feat(process_tracker): Invoke record back flow in PCR workflow [V2] (#7660)

- **Commit:** `40174b3c`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-04-02T11:59:15+05:30
- **Changes:** 7 files (+237/-34)

## 1342. feat(connector): Add recovery support for stripebilling (#7461)

- **Commit:** `cfe22694`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-04-02T12:48:19+05:30
- **Changes:** 34 files (+1044/-320)

## 1343. fix(connector): [JPMORGAN, PAYU, DIGITALVIRGO, BITPAY, HELCIM, PAYBOX] Replaced lazystatic macros with LazyLock (#7524)

- **Commit:** `fcbd863b`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-04-02T18:33:25+05:30
- **Changes:** 6 files (+272/-290)

## 1344. revert: implement `NameType` for name validation (#6734) (#7717)

- **Commit:** `d892ee7a`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-04-03T18:49:08+05:30
- **Changes:** 72 files (+364/-734)

## 1345. feat(core): add network error related columns in payment attempt [v2] (#7706)

- **Commit:** `5e9e9238`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-04-04T14:30:22+05:30
- **Changes:** 160 files (+1190/-690)

## 1346. fix(connector): [Nexixpay] handle error code and message in failure response (#7713)

- **Commit:** `f532b70a`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2025-04-04T18:25:15+05:30
- **Changes:** 1 files (+247/-132)

## 1347. feat(authentication): create authentications to fallback to ApiKeyAuth if AdminApiAuth fails (#7744)

- **Commit:** `d6c26c5d`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-04-08T13:19:01+05:30
- **Changes:** 5 files (+263/-108)

## 1348. feat(router): Support `card` in `payment_method_subtype` [V2] (#7662)

- **Commit:** `187cceb3`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-04-08T15:18:55+05:30
- **Changes:** 33 files (+340/-65)

## 1349. feat(connector): Add recovery support for recurly [v2] (#7497)

- **Commit:** `68e22eef`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-04-08T15:38:48+05:30
- **Changes:** 11 files (+310/-53)

## 1350. refactor: move merchant_key_store table to accounts schema (#7746)

- **Commit:** `e88672c9`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-04-08T17:19:46+05:30
- **Changes:** 13 files (+180/-38)

## 1351. feat(connector): [AIRWALLEX, ELAVON, NOVALNET, XENDIT] add in feature API (#7163)

- **Commit:** `98738d0b`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-04-08T18:01:48+05:30
- **Changes:** 11 files (+502/-113)

## 1352. feat(payment_link): expose configurations for payment links (#7742)

- **Commit:** `b475171d`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-04-09T12:46:15+05:30
- **Changes:** 16 files (+274/-10)

## 1353. fix(router): fix retry_count and add validation for process_tracker (#7614)

- **Commit:** `6ef71051`
- **Author:** Aditya Chaurasia <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-04-09T14:57:57+05:30
- **Changes:** 20 files (+401/-111)

## 1354. feat: remove client_secret from payment_intent and update related code (#7648)

- **Commit:** `5730ddfc`
- **Author:** Gaurav Rawat <104276743+GauravRawat369@users.noreply.github.com>
- **Date:** 2025-04-10T18:33:44+05:30
- **Changes:** 24 files (+84/-383)

## 1355. feat(webhook): add filter by event class and type (#7275)

- **Commit:** `989b2c34`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-04-11T15:45:23+05:30
- **Changes:** 12 files (+346/-219)

## 1356. fix(connector): Add network error message support for payment connectors (#7760)

- **Commit:** `b83e044b`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-04-11T15:47:13+05:30
- **Changes:** 8 files (+162/-58)

## 1357. feat(core): Add support for updating metadata after payment has been authorized (#7776)

- **Commit:** `92f68213`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-04-15T12:37:26+05:30
- **Changes:** 39 files (+1241/-59)

## 1358. refactor(customer): refactor customer db with storage utils and move trait to domain_models and impl to storage_model (#7538)

- **Commit:** `e8e0b5df`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-04-15T12:53:33+05:30
- **Changes:** 8 files (+1109/-1575)

## 1359. feat(vsaas): modify api key auth to support vsaas cases (#7593)

- **Commit:** `2a467053`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2025-04-16T15:48:56+05:30
- **Changes:** 24 files (+781/-190)

## 1360. feat(payment_method): add logic for setup_future_usage downgrade and add filter based on zero mandate config (#7775)

- **Commit:** `d061e0a7`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-04-17T17:08:18+05:30
- **Changes:** 27 files (+318/-33)

## 1361. refactor(required_fields): move pm required fields to pm crate (#7539)

- **Commit:** `103a5c18`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-04-21T13:26:58+05:30
- **Changes:** 12 files (+3480/-14515)

## 1362. feat(refunds_v2): Add refund create core flow (#7619)

- **Commit:** `eabef328`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-04-21T14:05:27+05:30
- **Changes:** 28 files (+1459/-134)

## 1363. feat(dynamic_routing): add open router integration for success based routing (#7795)

- **Commit:** `a51c9f03`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2025-04-21T19:30:19+05:30
- **Changes:** 12 files (+477/-43)

## 1364. feat(dynamic_routing): integration of elimination routing for core flows (#6816)

- **Commit:** `82bc4616`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-04-22T12:36:42+05:30
- **Changes:** 7 files (+463/-129)

## 1365. feat(vsaas): add processor_merchant_id and created_by column in payment_intents and payments_attempts for v1 (#7768)

- **Commit:** `6281ae06`
- **Author:** Uzair Khan <uzair.khan@juspay.in>
- **Date:** 2025-04-22T13:37:44+05:30
- **Changes:** 30 files (+591/-105)

## 1366. fix(connector): revert noon-paypal (#7864)

- **Commit:** `776bde00`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-04-22T16:38:29+05:30
- **Changes:** 11 files (+18/-483)

## 1367. feat(connector): [Facilitapay] Add support for Pix Bank Transfers (#7704)

- **Commit:** `639b8cba`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-04-23T13:36:17+05:30
- **Changes:** 37 files (+1621/-277)

## 1368. feat(users): add support for caching and resolving last used lineage context (#7871)

- **Commit:** `01bca772`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-04-23T19:06:28+05:30
- **Changes:** 5 files (+242/-14)

## 1369. refactor(connector): [BILLWERK, FISERVEMEA, TSYS] use LazyLock instead of lazy_static (#7494)

- **Commit:** `413a7eee`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-04-24T15:13:43+05:30
- **Changes:** 3 files (+104/-105)

## 1370. refactor(connector): [NMI,PAYONE,RISKIFIED] moved to hyperswitch_connectors (#7666)

- **Commit:** `b4610875`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-04-24T15:15:10+05:30
- **Changes:** 20 files (+1419/-1424)

## 1371. feat(payments): add support for connector testing (Adyen) (#7874)

- **Commit:** `f1bb4a09`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-04-24T20:30:10+05:30
- **Changes:** 12 files (+256/-51)

## 1372. feat(connector): [GETNET,HIPAY,KLARNA,MONERIS,OPENNODE] add in feature matrix api (#7873)

- **Commit:** `69ba651a`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-04-25T14:53:05+05:30
- **Changes:** 12 files (+452/-100)

## 1373. feat(core): Add cardbrand union fetch logic for click to pay session response (#7858)

- **Commit:** `d2ff66bb`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-04-28T16:54:15+05:30
- **Changes:** 16 files (+193/-56)

## 1374. feat(core): Adds Billing Connector Invoice Sync flow in Revenue Recovery (#7799)

- **Commit:** `3d0dd5bd`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-04-29T12:25:31+05:30
- **Changes:** 14 files (+294/-34)

## 1375. feat(merchant_context): add struct `merchant_context` and replace all instances of `merchant_account` and `key_store` in core (#7882)

- **Commit:** `693f9019`
- **Author:** Uzair Khan <uzair.khan@juspay.in>
- **Date:** 2025-04-29T14:41:21+05:30
- **Changes:** 139 files (+4718/-4299)

## 1376. feat(process_tracker): Task implementation for psync payments (#7178)

- **Commit:** `9e9a9229`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2025-04-30T13:23:54+05:30
- **Changes:** 19 files (+1115/-417)

## 1377. feat(connector): [MULTISAFEPAY, CASHTOCODE, WORLDPAY, WELLSFARGO] Supported features for feature matrix (#7149)

- **Commit:** `8c77da7a`
- **Author:** Debarshi Gupta <debarshigupta47@gmail.com>
- **Date:** 2025-04-30T14:29:18+05:30
- **Changes:** 10 files (+578/-147)

## 1378. feat(connector): [Recurly] add invoice sync support along with transaction monitoring  (#7867)

- **Commit:** `bcc57ebb`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-05-02T17:10:48+05:30
- **Changes:** 31 files (+823/-1167)

## 1379. feat(connector): Fix Serde derserialization issue -Elavon/Adyen (#7823)

- **Commit:** `78892257`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-05-05T15:47:50+05:30
- **Changes:** 4 files (+219/-66)

## 1380. feat(connector): [globalpay, globepay, itaubank, nexinets, nuvei, prophetpay, zen] add in feature matrix (#7258)

- **Commit:** `7c17996c`
- **Author:** sweta-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-05-06T12:32:31+05:30
- **Changes:** 14 files (+1059/-92)

## 1381. Refactor(connector): Migrate [AdyenPlatform, Ebanx, GPayments, Netcetera, Plaid] from crates/router to crates/hyperswitch_connectors (#7913)

- **Commit:** `b024c411`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-05-06T12:36:14+05:30
- **Changes:** 30 files (+2981/-2949)

## 1382. feat(connector): [FEATURE MATRIX] Connector feature matrix (#7147)

- **Commit:** `15df5ac6`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-05-06T12:38:13+05:30
- **Changes:** 11 files (+434/-20)

## 1383. feat(refunds_v2): Add Refunds Retrieve and Refunds Sync Core flow (#7835)

- **Commit:** `a289f19c`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-05-07T12:04:39+05:30
- **Changes:** 12 files (+470/-14)

## 1384. fix(update_metadata): Update Metadata for any connectors other than stripe gives 500 error (#7984)

- **Commit:** `fafe4d99`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-05-08T16:37:30+05:30
- **Changes:** 2 files (+201/-13)

## 1385. feat(connector): [paypal, trustpay] add in feature matrix (#7911)

- **Commit:** `a64a4d59`
- **Author:** sweta-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-05-08T17:27:24+05:30
- **Changes:** 9 files (+411/-23)

## 1386. refactor(authentication): moved cavv storing from table to temp locker (#7978)

- **Commit:** `dbaf5679`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-05-12T16:54:55+05:30
- **Changes:** 21 files (+307/-93)

## 1387. feat(payment_methods): add v2 api for fetching token data (#7629)

- **Commit:** `2cefac5c`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-05-12T19:15:53+05:30
- **Changes:** 16 files (+486/-16)

## 1388. refactor(open_router): call elimination routing of open router if enabled instead of dynamo (#7961)

- **Commit:** `bab64eef`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2025-05-12T19:16:08+05:30
- **Changes:** 6 files (+213/-171)

## 1389. feat(connector): [ADYEN, CHECKOUT] Added In Feature Matrix API (#7914)

- **Commit:** `e404c0ce`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-05-12T19:18:16+05:30
- **Changes:** 9 files (+973/-6)

## 1390. feat(connector): Introduce connector template code for WorldpayXML  (#7968)

- **Commit:** `57cb3a9f`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-05-12T19:18:51+05:30
- **Changes:** 23 files (+1324/-5)

## 1391. feat(vsaas): integrate onboarding flow for vertical saas (#7884)

- **Commit:** `cf34be17`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2025-05-12T19:19:42+05:30
- **Changes:** 22 files (+376/-33)

## 1392. feat(refunds_v2): Add refunds list flow in v2 apis (#7966)

- **Commit:** `839eb2e8`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-05-12T19:27:05+05:30
- **Changes:** 14 files (+716/-17)

## 1393. feat(connector): [ACI, AUTHORIZEDOTNET, BRAINTREE, FIUU, FORTE, PLACETOPAY] Supported features for feature matrix (#7854)

- **Commit:** `32bbad90`
- **Author:** Chaitak Gorai <77141674+chaitak-gorai@users.noreply.github.com>
- **Date:** 2025-05-12T20:05:11+05:30
- **Changes:** 12 files (+939/-174)

## 1394. feat(routing): Add support to update config for elimination routing (#7938)

- **Commit:** `d07a85ca`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2025-05-12T21:02:24+05:30
- **Changes:** 5 files (+222/-17)

## 1395. feat(users): store and retrieve lineage_context from DB instead of Redis (#7940)

- **Commit:** `6f22a930`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-05-13T12:53:10+05:30
- **Changes:** 27 files (+186/-145)

## 1396. refactor(paymentMethods): move all pm migration related changes to payment methods crate (#7786)

- **Commit:** `9c8cf936`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-05-13T13:39:52+05:30
- **Changes:** 40 files (+3386/-3037)

## 1397. feat(refunds_v2): Add refund update core flow in v2 apis (#7724)

- **Commit:** `04dc14a9`
- **Author:** Amey Wale <76102448+AmeyWale@users.noreply.github.com>
- **Date:** 2025-05-13T14:36:22+05:30
- **Changes:** 8 files (+239/-22)

## 1398. refactor(Connector): [signifyd,threedsecureio,wellsfargopayout,wise] move from routers to hyperswitch_connectors (#7953)

- **Commit:** `1dabfe3e`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-05-13T14:59:39+05:30
- **Changes:** 24 files (+2378/-2510)

## 1399. chore(users): add hubspot tracking to prod intent (#7798)

- **Commit:** `67f38f86`
- **Author:** Riddhiagrawal001 <50551695+Riddhiagrawal001@users.noreply.github.com>
- **Date:** 2025-05-13T17:25:27+05:30
- **Changes:** 36 files (+923/-420)

## 1400. feat(router): add outgoing payment webhooks for v2 (#6613)

- **Commit:** `aa6ebf8a`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-05-14T00:13:33+05:30
- **Changes:** 11 files (+1196/-34)

## 1401. refactor: remove unused functions (#7994)

- **Commit:** `46e830a8`
- **Author:** Surya <110617981+Surya-7890@users.noreply.github.com>
- **Date:** 2025-05-14T15:28:37+05:30
- **Changes:** 1 files (+0/-255)

## 1402. feat(connector_cloning): Create API for cloning connectors between merchants and profiles. (#7949)

- **Commit:** `82f15e95`
- **Author:** Mani Chandra <84711804+ThisIsMani@users.noreply.github.com>
- **Date:** 2025-05-14T20:33:40+05:30
- **Changes:** 25 files (+493/-87)

## 1403. feat(euclid): integration with decision engine (#7930)

- **Commit:** `4087cd27`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-05-14T23:38:59+05:30
- **Changes:** 13 files (+882/-8)

## 1404. feat(core): Add Support for redirection inside Iframe  (#7976)

- **Commit:** `831149c9`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-05-15T15:33:54+05:30
- **Changes:** 29 files (+288/-17)

## 1405. feat(router): Add support for Vault in connector_accounts endpoint (#7814)

- **Commit:** `89b421f8`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-05-15T15:36:44+05:30
- **Changes:** 26 files (+1376/-7)

## 1406. feat(connector): revert [paypal, trustpay] add in feature matrix (#8042)

- **Commit:** `5fd6df73`
- **Author:** sweta-sharma <77436883+Sweta-Kumari-Sharma@users.noreply.github.com>
- **Date:** 2025-05-15T18:12:31+05:30
- **Changes:** 9 files (+23/-411)

## 1407. feat(connector): Archipel connector (#7851)

- **Commit:** `3d095cec`
- **Author:** michal-czernecki <michal.czernecki@flowbird.group>
- **Date:** 2025-05-16T11:21:29+02:00
- **Changes:** 468 files (+27027/-67)

## 1408. refactor(connector): stripe migration from router to hyperswitch_connectors (#8007)

- **Commit:** `e5cf6698`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-05-16T19:20:04+05:30
- **Changes:** 15 files (+1733/-2613)

## 1409. feat: add support for 3ds exemption rules in euclid crate (#8013)

- **Commit:** `34dd99d8`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-05-16T19:24:13+05:30
- **Changes:** 9 files (+371/-34)

## 1410. feat(router): add open router integration for debit routing (#7907)

- **Commit:** `140d15bc`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-05-19T15:34:29+05:30
- **Changes:** 61 files (+1426/-171)

## 1411. feat(core): [Network Tokenization] pre network tokenization (#6873)

- **Commit:** `da90d74b`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-05-19T15:52:12+05:30
- **Changes:** 17 files (+593/-100)

## 1412. build(deps): migrate usages of `once_cell` crate to standard library equivalents (#8030)

- **Commit:** `673cf249`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2025-05-19T15:54:03+05:30
- **Changes:** 32 files (+176/-183)

## 1413. feat(core): add all_keys_required in confirm and psync payload (#7998)

- **Commit:** `071b0732`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-05-19T18:57:43+05:30
- **Changes:** 81 files (+353/-15)

## 1414. feat(connector): add barclaycard template code (#8017)

- **Commit:** `6e08edca`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-05-20T17:14:25+05:30
- **Changes:** 24 files (+1348/-24)

## 1415. feat(reveue_recovery): Add support for multiple retry algorithms in revenue recovery workflow (#7915)

- **Commit:** `151b57fa`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2025-05-20T18:02:47+05:30
- **Changes:** 18 files (+220/-63)

## 1416. feat(core): add a procedural macro for validating schema attributes for a struct (#8006)

- **Commit:** `4332299a`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-05-20T21:27:01+05:30
- **Changes:** 12 files (+518/-9)

## 1417. feat(connector): [nordea] template code (#8056)

- **Commit:** `7c1d893c`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-05-21T12:45:46+05:30
- **Changes:** 24 files (+1331/-16)

## 1418. feat(payment_methods): add external vault connector service (#7917)

- **Commit:** `1238ae77`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-05-21T17:14:51+05:30
- **Changes:** 39 files (+1521/-73)

## 1419. chore(openapi): resolve openapi  semantic inconsistency (#8099)

- **Commit:** `fa4b552a`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-05-22T15:21:54+05:30
- **Changes:** 9 files (+233/-71)

## 1420. feat(router): Add support for Proxy api (#7901)

- **Commit:** `8e9bad64`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-05-22T18:31:36+05:30
- **Changes:** 22 files (+707/-34)

## 1421. feat(dynamic_routing): Decision engine config API integration  (#8044)

- **Commit:** `d41f6538`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-05-22T23:42:40+05:30
- **Changes:** 9 files (+885/-96)

## 1422. feat(tokenio): Add Template PR (#8095)

- **Commit:** `9f9fef49`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-05-23T14:37:52+05:30
- **Changes:** 23 files (+1331/-9)

## 1423. feat(connector): [XENDIT] Added Integrity Check for Authorize, Capture, Refund & RSync flows (#8049)

- **Commit:** `caa07235`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-05-23T14:51:00+05:30
- **Changes:** 4 files (+173/-100)

## 1424. feat(core): add one-way TLS support with CA certificate for ArchiPEL UAT environment (#8128)

- **Commit:** `e6558329`
- **Author:** Debarati Ghatak <88573135+cookieg13@users.noreply.github.com>
- **Date:** 2025-05-25T20:55:28+05:30
- **Changes:** 13 files (+101/-11206)

## 1425. feat(router): adding generic tokenization endpoint (#7905)

- **Commit:** `49a178ed`
- **Author:** Shivansh Mathur <104988143+su-shivanshmathur@users.noreply.github.com>
- **Date:** 2025-05-27T11:39:36+05:30
- **Changes:** 60 files (+1450/-38)

## 1426. feat(connector): Stripe revolut pay wallet integration (#8066)

- **Commit:** `b3d47b65`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-05-27T12:07:44+05:30
- **Changes:** 52 files (+165/-42)

## 1427. feat(connector): [Worldpayxml] add card payment (#8076)

- **Commit:** `b8b68af4`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-05-27T14:39:55+05:30
- **Changes:** 20 files (+1921/-210)

## 1428. feat(connector): [Barclaycard] Implement Cards - Non 3DS flow (#8068)

- **Commit:** `01af4742`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-05-27T15:24:39+05:30
- **Changes:** 20 files (+2219/-221)

## 1429. feat: list for dynamic routing (#8111)

- **Commit:** `a6546950`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-05-27T15:31:08+05:30
- **Changes:** 18 files (+790/-264)

## 1430. refactor: Payment Attempt as mandatory field in PaymentStatusData (#8126)

- **Commit:** `eb15fa11`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-05-29T15:24:05+05:30
- **Changes:** 9 files (+112/-122)

## 1431. feat(vsaas): enable platform merchant API Key authentication for org-level operations (#8156)

- **Commit:** `7a446262`
- **Author:** Sandeep Kumar <83278309+tsdk02@users.noreply.github.com>
- **Date:** 2025-05-30T18:20:40+05:30
- **Changes:** 10 files (+549/-44)

## 1432. feat(router): add three_ds_decision_rule support in routing apis (#8132)

- **Commit:** `9bac41b2`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-05-30T18:21:35+05:30
- **Changes:** 19 files (+395/-93)

## 1433. feat(core): Altered the amount field in DisputePayload to StringMinorUnit (#8131)

- **Commit:** `04763612`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-05-30T19:56:08+05:30
- **Changes:** 37 files (+356/-126)

## 1434. build(deps): bump dependencies to compatible versions (#8164)

- **Commit:** `9a9fb3de`
- **Author:** Sanchith Hegde <22217505+SanchithHegde@users.noreply.github.com>
- **Date:** 2025-06-01T02:43:27+05:30
- **Changes:** 38 files (+1451/-1202)

## 1435. feat(connector): [FISERV] Added Integrity Check support for all Payment & Refund Flows (#8075)

- **Commit:** `dbca363f`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-02T12:06:08+05:30
- **Changes:** 2 files (+223/-49)

## 1436. feat(analytics): revamped 3ds auth analytics (#8163)

- **Commit:** `55f6dbe3`
- **Author:** Sanskar Atrey <sanskaratrey22@gmail.com>
- **Date:** 2025-06-02T15:08:00+05:30
- **Changes:** 23 files (+1309/-3)

## 1437. feat(routing): Add audit trail for routing (#8188)

- **Commit:** `ebe44b9d`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-06-03T02:23:56+05:30
- **Changes:** 27 files (+1373/-34)

## 1438. feat(payments): implement routing in payments v2 (#7709)

- **Commit:** `8871f310`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-06-03T12:33:39+05:30
- **Changes:** 20 files (+532/-114)

## 1439. feat(connectors): [Template] add Worldpayvantiv  (#8226)

- **Commit:** `fd844c3d`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-06-04T15:30:32+05:30
- **Changes:** 23 files (+1339/-5)

## 1440. feat(connectors): [Worldpayvantiv] add card support (#8219)

- **Commit:** `f5c4f610`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-06-04T19:26:42+05:30
- **Changes:** 21 files (+3018/-260)

## 1441. feat(payment_methods): add `external_vault_details` for payments v2 sdk session call (#8003)

- **Commit:** `d32c61a2`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-06-06T17:31:08+05:30
- **Changes:** 58 files (+2308/-100)

## 1442. feat(router): Save payment method on payments confirm (V2) (#8090)

- **Commit:** `2c356397`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-06-06T20:54:31+05:30
- **Changes:** 26 files (+1057/-113)

## 1443. feat(router): add three_ds decision rule execute api (#8148)

- **Commit:** `e90a95de`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-06-06T21:50:34+05:30
- **Changes:** 31 files (+1062/-9)

## 1444. feat(connector): [STRIPE] Added Connector Tokenization Flow for Cards (#8248)

- **Commit:** `81292602`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-07T19:46:13+05:30
- **Changes:** 8 files (+223/-131)

## 1445. ci(postman): add tunnel collection to postman tests (#8269)

- **Commit:** `e58eeb1a`
- **Author:** likhinbopanna <131246334+likhinbopanna@users.noreply.github.com>
- **Date:** 2025-06-08T19:14:03+05:30
- **Changes:** 60 files (+3007/-0)

## 1446. feat(tokenio): Add OpenBanking Redirection Flow (#8152)

- **Commit:** `4c73d748`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-06-09T13:40:27+05:30
- **Changes:** 33 files (+2818/-524)

## 1447. fix(connector): [jpmorgan] 5xx during payment authorize and `cancellation_reason` (#8282)

- **Commit:** `80206eed`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-06-10T13:54:15+05:30
- **Changes:** 4 files (+410/-9)

## 1448. feat(core): Make installment_payment_enabled,recurring_enabled Optional (#8201)

- **Commit:** `171ca3b5`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-06-10T16:01:50+05:30
- **Changes:** 17 files (+149/-120)

## 1449. feat(connector): [TRUSTPAY] Added Integrity Checks for PSync & RSync flows & Added New Variants in AttemptStatus & IntentStatus (#8096)

- **Commit:** `a76a9c15`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-10T22:00:18+05:30
- **Changes:** 31 files (+148/-64)

## 1450. docs: Improving API Reference (#8194)

- **Commit:** `5ce2ab2d`
- **Author:** GORAKHNATH YADAV <gorakhcodes@gmail.com>
- **Date:** 2025-06-11T15:24:45+05:30
- **Changes:** 9 files (+1399/-673)

## 1451. feat(authentication): added profile acquirer create module (#8155)

- **Commit:** `f54d785e`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-06-11T18:50:19+05:30
- **Changes:** 32 files (+699/-22)

## 1452. feat(connector): Implement Razorpay UPI Collect (#8009)

- **Commit:** `ee7bce0f`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-06-11T18:55:24+05:30
- **Changes:** 50 files (+1402/-1466)

## 1453. refactor(router): Remove `payment_methods_v2` and `customer_v2` feature flag (#8236)

- **Commit:** `000aa23c`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-06-12T00:07:24+05:30
- **Changes:** 106 files (+896/-1856)

## 1454. feat(router): add `merchant_category_code` in business profile (#8296)

- **Commit:** `0f142798`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-06-12T15:35:50+05:30
- **Changes:** 17 files (+254/-4)

## 1455. feat(authentication): create api for update profile acquirer (#8307)

- **Commit:** `d33e344f`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-06-12T17:39:15+05:30
- **Changes:** 14 files (+416/-23)

## 1456. refactor(debit_routing): filter debit networks based on merchant connector account configuration (#8175)

- **Commit:** `5f97b7bc`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-06-12T18:12:37+05:30
- **Changes:** 1 files (+245/-64)

## 1457. feat(connector): [trustpay] introduce instant bank_transfer, finland and poland (#7925)

- **Commit:** `61c2e2c7`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-06-13T12:03:32+05:30
- **Changes:** 53 files (+600/-141)

## 1458. docs(openapi): Show API version selection dropdown in Mintlify (#8333)

- **Commit:** `ce85b838`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-06-13T14:00:38+05:30
- **Changes:** 224 files (+468/-1159)

## 1459. feat: migration api for migrating routing rules to decision_engine (#8233)

- **Commit:** `9045eb5b`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-06-13T14:34:24+05:30
- **Changes:** 10 files (+318/-5)

## 1460. feat(core): consume card details from billing connectors and first error codes and store them in payment intent table (#8250)

- **Commit:** `abe9708d`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-06-16T16:36:59+05:30
- **Changes:** 16 files (+403/-34)

## 1461. refactor(routing): Routing events core refactor (#8323)

- **Commit:** `4d36be87`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-06-17T19:46:05+05:30
- **Changes:** 6 files (+1534/-739)

## 1462. feat(core): accept merchant_connector_details in Payments and Psync flow (#8199)

- **Commit:** `b8b19605`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-06-17T20:51:57+05:30
- **Changes:** 44 files (+938/-360)

## 1463. fix(connector): [STRIPE] Retrieving Connect Account Id from Mandate Metadata in MITs (#8326)

- **Commit:** `17c30b61`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-18T17:21:14+05:30
- **Changes:** 11 files (+229/-31)

## 1464. fix(connectors): [worldpayvantiv] change endpoint, add billing address and fix 5xx incase of psync (#8354)

- **Commit:** `5f7055fc`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-06-19T12:04:32+05:30
- **Changes:** 8 files (+301/-209)

## 1465. feat(kafka): add payment_intent payment_attempt and refund kafka events for v2 (#8328)

- **Commit:** `305ca9bd`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-06-19T12:06:07+05:30
- **Changes:** 12 files (+1138/-332)

## 1466. feat(router): Add v2 endpoint to list payment attempts by intent_id (#8368)

- **Commit:** `7943fb4b`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-06-20T11:55:06+05:30
- **Changes:** 15 files (+719/-12)

## 1467. feat(routing): add profile config to switch between HS routing and DE routing result (#8350)

- **Commit:** `a721d90c`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-06-20T18:19:23+05:30
- **Changes:** 7 files (+710/-390)

## 1468. fix(openapi): correct schema references and semantics for v1 openApi spec (#8127)

- **Commit:** `02dee9c5`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-06-20T18:21:27+05:30
- **Changes:** 19 files (+296/-474)

## 1469. feat(connector): [DUMMY_CONNECTOR] crate restructuring (#8372)

- **Commit:** `293d93f6`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-06-20T18:21:43+05:30
- **Changes:** 11 files (+1283/-1407)

## 1470. feat(connector): [SANTANDER] Add Template Code (#8369)

- **Commit:** `c8b35dac`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-20T18:21:54+05:30
- **Changes:** 24 files (+1342/-12)

## 1471. docs(connector): [STRIPE] Added CIT & MIT Examples for API Reference in Stripe Split Payments (#8311)

- **Commit:** `0851c6ec`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-20T18:29:46+05:30
- **Changes:** 2 files (+360/-38)

## 1472. chore: resolve warnings in v2 (#8373)

- **Commit:** `d2d4f3d1`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-06-22T16:58:23+05:30
- **Changes:** 50 files (+218/-320)

## 1473. fix(connector): [NEXIXPAY] Add Validation Checks for Request Fields (#8345)

- **Commit:** `6fd7626c`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-06-23T15:07:31+05:30
- **Changes:** 6 files (+323/-95)

## 1474. feat(router): add `apply_three_ds_strategy` in payments confirm flow (#8357)

- **Commit:** `786fe699`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-06-23T19:29:24+05:30
- **Changes:** 8 files (+215/-13)

## 1475. feat(analytics): Add RoutingApproach filter in payment analytics (#8408)

- **Commit:** `a3cc44c6`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-06-23T22:53:42+05:30
- **Changes:** 54 files (+406/-65)

## 1476. feat(authentication): Initial commit to modular authentication create (#8085)

- **Commit:** `2ea5d81d`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-06-24T17:03:24+05:30
- **Changes:** 45 files (+948/-132)

## 1477. refactor: Move CustomerAcceptance to common_types (#8299)

- **Commit:** `44d93e57`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-06-25T11:27:09+05:30
- **Changes:** 35 files (+194/-267)

## 1478. refactor(router): Remove `refunds_v2` feature flag (#8310)

- **Commit:** `c5c0e677`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-06-25T15:50:42+05:30
- **Changes:** 24 files (+362/-482)

## 1479. feat(router): Add webhooks for network tokenization  (#6695)

- **Commit:** `ec6d0e4d`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-06-26T14:43:04+05:30
- **Changes:** 25 files (+903/-26)

## 1480. feat: Kv changes for V2 feature (#8198)

- **Commit:** `d2740f03`
- **Author:** akshay-97 <adiosphobian@gmail.com>
- **Date:** 2025-06-26T19:15:22+05:30
- **Changes:** 15 files (+868/-113)

## 1481. feat(core): accept merchant_connector_details in Refunds create and retrieve flow (#8441)

- **Commit:** `b185d85f`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-06-26T19:20:00+05:30
- **Changes:** 13 files (+438/-91)

## 1482. feat(core): allow setting up status across payments, refunds and payouts for triggering webhooks in core resource flows (#8433)

- **Commit:** `d305fad2`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-06-30T12:38:04+05:30
- **Changes:** 20 files (+546/-190)

## 1483. feat(connector): Implement capture and webhook flow, fix some issues in ACI (#8349)

- **Commit:** `1ae30247`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-07-01T14:50:45+05:30
- **Changes:** 6 files (+582/-49)

## 1484. feat(data-migration): add connector customer and mandate details support for multiple profiles (#8473)

- **Commit:** `ce2b90b3`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-07-01T15:02:24+05:30
- **Changes:** 9 files (+437/-174)

## 1485. feat(connectors): [Worldpayvantiv] add NTI flow and refactor sync flows (#8495)

- **Commit:** `f8dc3ecf`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-07-01T16:18:36+05:30
- **Changes:** 10 files (+414/-1936)

## 1486. feat(connector): [ADYENPLATFORM] add card payouts (#8504)

- **Commit:** `0c649158`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-07-01T16:30:42+05:30
- **Changes:** 2 files (+194/-86)

## 1487. refactor: exposed auth analytics at merchant,org and profile levels (#8335)

- **Commit:** `e638f239`
- **Author:** Sanskar Atrey <sanskaratrey22@gmail.com>
- **Date:** 2025-07-01T16:51:35+05:30
- **Changes:** 17 files (+368/-200)

## 1488. feat(connector): [DWOLLA] - Add template code (#8496)

- **Commit:** `ad522513`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-07-01T16:52:47+05:30
- **Changes:** 24 files (+1333/-9)

## 1489. refactor(authentication): flattened paymentData in authentication trait functions (#8365)

- **Commit:** `18a779f9`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-07-01T18:46:15+05:30
- **Changes:** 7 files (+142/-107)

## 1490. feat(payouts): add domain type for PayoutId (#8395)

- **Commit:** `a6e3d2c7`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-07-01T19:12:01+05:30
- **Changes:** 58 files (+506/-269)

## 1491. refactor(connector): update add connector script with new connector features (#8213)

- **Commit:** `2ff93ff9`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-07-01T19:34:18+05:30
- **Changes:** 5 files (+209/-57)

## 1492. feat(connector): [SANTANDER] Added Authorize, PSync, Void, Refund & RSync Flows for Pix QR Code Bank Transfer  (#8463)

- **Commit:** `28d63575`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-07-01T19:44:08+05:30
- **Changes:** 24 files (+1116/-185)

## 1493. chore: address Rust 1.88.0 clippy lints (#8498)

- **Commit:** `20b52f11`
- **Author:** Chethan Rao <70657455+Chethan-rao@users.noreply.github.com>
- **Date:** 2025-07-02T12:13:07+05:30
- **Changes:** 150 files (+464/-647)

## 1494. feat(connector): [CHECKBOOK] Add Template Code (#8494)

- **Commit:** `95077c64`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-07-02T15:24:29+05:30
- **Changes:** 24 files (+1357/-28)

## 1495. feat(connector): [shift4] Boleto, Trustly, Alipay, Wechatpay PMs added (#8476)

- **Commit:** `ac3b2d40`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-07-03T13:18:10+05:30
- **Changes:** 9 files (+185/-34)

## 1496. feat(connector): [payload] template code (#8526)

- **Commit:** `7f5ec743`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-07-03T13:31:22+05:30
- **Changes:** 28 files (+1470/-27)

## 1497. feat(core): populate connector raw response and connector_response_reference_id for razorpay (#8499)

- **Commit:** `2253d981`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-07-03T17:18:33+05:30
- **Changes:** 53 files (+576/-408)

## 1498. feat(connector): [Redsys] Use merchant payment_id for ds_merchant_order with length check (#8485)

- **Commit:** `6678ee35`
- **Author:** Saptak Dutta <138141940+Saptak88@users.noreply.github.com>
- **Date:** 2025-07-03T21:55:45+05:30
- **Changes:** 49 files (+346/-45)

## 1499. refactor: extract connector auth and metadata validation into separate module (#8501)

- **Commit:** `26ae469f`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-07-04T16:32:29+05:30
- **Changes:** 4 files (+592/-585)

## 1500. feat(debit_routing): add `debit_routing_savings` in analytics payment attempt (#8519)

- **Commit:** `fc3c64fa`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-07-04T19:11:06+05:30
- **Changes:** 26 files (+617/-44)

## 1501. refactor(connector): [Worldpayvantiv] refactor void flow and handle transaction status (#8540)

- **Commit:** `41291e5c`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-07-04T19:13:03+05:30
- **Changes:** 2 files (+1787/-87)

## 1502. feat(core): Hyperswitch <|> UCS Integration (#8280)

- **Commit:** `f6574b78`
- **Author:** Debarshi Gupta <debarshi.gupta@juspay.in>
- **Date:** 2025-07-04T22:38:20+05:30
- **Changes:** 36 files (+1563/-427)

## 1503. feat(connector): [payload] introduce no-3ds cards (#8545)

- **Commit:** `baad3f6a`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-07-05T20:06:32+05:30
- **Changes:** 14 files (+1298/-179)

## 1504. feat(connector): [Celero] add Connector Template Code (#8489)

- **Commit:** `dfed2be2`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-07-07T16:52:50+05:30
- **Changes:** 25 files (+1419/-90)

## 1505. feat(connectors): [worldpayvantiv] add connector mandate support  (#8546)

- **Commit:** `de92973b`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-07-07T17:04:48+05:30
- **Changes:** 3 files (+185/-77)

## 1506. feat(connector): [silverflow] template code (#8553)

- **Commit:** `c322eb9c`
- **Author:** Yashasvi Kapil <74726400+iemyashasvi@users.noreply.github.com>
- **Date:** 2025-07-08T13:08:14+05:30
- **Changes:** 22 files (+1385/-12)

## 1507. feat(connector): [AUTHIPAY] Integrate cards non 3ds payments (#8266)

- **Commit:** `ef42ad43`
- **Author:** Yashasvi Kapil <74726400+iemyashasvi@users.noreply.github.com>
- **Date:** 2025-07-08T17:31:09+05:30
- **Changes:** 32 files (+3099/-25)

## 1508. refactor(connector): Move connector mappings and endpoints to dedicated modules (#8562)

- **Commit:** `99885b69`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-07-09T13:04:41+05:30
- **Changes:** 16 files (+659/-639)

## 1509. feat(connector): [AIRWALLEX] - Added Paypal, Trustly, Klarna , Atome, Blik Payment Methods (#8475)

- **Commit:** `d5f55274`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-07-11T12:36:44+05:30
- **Changes:** 10 files (+697/-85)

## 1510. feat(connector): [payload] add webhook support (#8558)

- **Commit:** `2fe3132d`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-07-11T17:55:18+05:30
- **Changes:** 8 files (+262/-110)

## 1511. feat(core): Hyperswitch <|> UCS integration v2 (#8439)

- **Commit:** `ae9feca8`
- **Author:** Uzair Khan <29498864+maverox@users.noreply.github.com>
- **Date:** 2025-07-11T19:41:13+05:30
- **Changes:** 13 files (+1060/-387)

## 1512. feat(connector): [Multisafepay] Integrate EPS, MBWAY and SOFORT (#8506)

- **Commit:** `8a9d7d22`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-07-14T14:55:59+05:30
- **Changes:** 8 files (+200/-18)

## 1513. feat(connector): Add Incremental Authorization flow for Paypal (#8517)

- **Commit:** `fd6de7cc`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-07-14T16:21:00+05:30
- **Changes:** 13 files (+429/-61)

## 1514. feat(business_profile): added merchant country code in business profile (#8529)

- **Commit:** `44f8964a`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-07-14T17:25:37+05:30
- **Changes:** 20 files (+235/-45)

## 1515. feat(router): Deduplicate PML response and populate bank details (V2) (#8583)

- **Commit:** `7d54ce87`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-07-14T17:40:28+05:30
- **Changes:** 6 files (+226/-63)

## 1516. feat(payment_methods): [Paysera, Skrill] Add support to paysera and skrill wallets and in shift4  (#8487)

- **Commit:** `45e2d5c1`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-07-15T13:05:00+05:30
- **Changes:** 53 files (+246/-5)

## 1517. feat(connector): [AFFIRM] add Connector Template Code (#8650)

- **Commit:** `9bc02516`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-07-16T15:36:04+05:30
- **Changes:** 21 files (+1375/-13)

## 1518. feat(ai): add endpoints to chat with ai service (#8585)

- **Commit:** `3d60e6c4`
- **Author:** Apoorv Dixit <64925866+apoorvdixit88@users.noreply.github.com>
- **Date:** 2025-07-17T01:30:13+05:30
- **Changes:** 26 files (+252/-6)

## 1519. refactor(router): decrypt the wallet token before the debit routing call (#8598)

- **Commit:** `bf8dc495`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-07-18T17:53:13+05:30
- **Changes:** 18 files (+473/-222)

## 1520. feat(debit_routing): add debit routing support for apple pay (#8673)

- **Commit:** `d42fad73`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-07-18T19:49:24+05:30
- **Changes:** 5 files (+249/-59)

## 1521. feat(connector): [BLACKHAWKNETWORK] Add Template Code  (#8632)

- **Commit:** `7f6a1266`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-07-21T13:39:51+05:30
- **Changes:** 22 files (+8269/-6881)

## 1522. feat(authentication): Added eligibility flow for modular authentication (#8431)

- **Commit:** `82eb3ca7`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-07-21T17:08:12+05:30
- **Changes:** 29 files (+1568/-173)

## 1523. refactor(payments): fetch payment method information in attempts list api v2 and add custom billing connector template (#8681)

- **Commit:** `110beaff`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-07-22T00:38:33+05:30
- **Changes:** 21 files (+1365/-36)

## 1524. feat(connector): Add template code for breadpay (#8655)

- **Commit:** `b2ab9277`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-07-21T23:52:12-07:00
- **Changes:** 22 files (+1420/-55)

## 1525. fix(openapi): Added Error Response Schema for Status Code 400 (#8684)

- **Commit:** `a01d6083`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-07-22T12:23:36+05:30
- **Changes:** 8 files (+248/-55)

## 1526. feat(connector): [SILVERFLOW] Integrate cards non 3ds payments (#8591)

- **Commit:** `b5219519`
- **Author:** Yashasvi Kapil <74726400+iemyashasvi@users.noreply.github.com>
- **Date:** 2025-07-24T11:39:55+05:30
- **Changes:** 6 files (+1114/-170)

## 1527. feat(connector):  [TRUSTPAYMENTS] Add Template Code  (#8672)

- **Commit:** `31590718`
- **Author:** Ayush Anand <114248859+ayush22667@users.noreply.github.com>
- **Date:** 2025-07-24T12:38:09+05:30
- **Changes:** 22 files (+1386/-8)

## 1528. feat(connector): [AIRWALLEX] Added Ideal & Skrill payment methods  (#8535)

- **Commit:** `15d589d2`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-07-24T12:43:23+05:30
- **Changes:** 40 files (+617/-55)

## 1529. feat(connector): [Breadpay]Add support for Breadpay connector (#8676)

- **Commit:** `0d9750cd`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-07-24T07:35:52-07:00
- **Changes:** 36 files (+595/-154)

## 1530. feat(connector): [Flexiti]template code for flexiti connector (#8714)

- **Commit:** `0f66692e`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-07-25T00:07:36-07:00
- **Changes:** 22 files (+1382/-20)

## 1531. feat(connector): [MPGS] template code (#8544)

- **Commit:** `98d924bf`
- **Author:** Kuntimaddi Manideep <kuntimaddi.manideep@juspay.in>
- **Date:** 2025-07-25T14:48:05+05:30
- **Changes:** 22 files (+1395/-33)

## 1532. feat(authentication): add authentication api for modular authentication (#8459)

- **Commit:** `dbdf7579`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-07-25T14:58:15+05:30
- **Changes:** 16 files (+759/-78)

## 1533. feat(recovery-events): add revenue recovery topic and vector config to push these events to s3 (#8285)

- **Commit:** `17d34a29`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-07-25T17:16:50+05:30
- **Changes:** 22 files (+612/-37)

## 1534. feat(themes): Create user APIs for managing themes (#8387)

- **Commit:** `20049d52`
- **Author:** Kanika Bansal <kanika.bansal@juspay.in>
- **Date:** 2025-07-28T13:02:37+05:30
- **Changes:** 18 files (+842/-32)

## 1535. feat(core): Hyperswitch <|> UCS Mandate flow integration (#8738)

- **Commit:** `f94f39ef`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-07-28T13:17:25+05:30
- **Changes:** 8 files (+773/-203)

## 1536. feat(connector): [BLUECODE] Added Template Code (#8756)

- **Commit:** `9f6182b7`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-07-29T13:29:33+05:30
- **Changes:** 28 files (+1416/-32)

## 1537. feat(connector): [FISERV] Added GooglePay Payment Method - Connector Decryption Flow (#8658)

- **Commit:** `b5586b68`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-07-29T13:30:24+05:30
- **Changes:** 11 files (+381/-64)

## 1538. feat(connector): [Adyen] receive incoming webhooks for pix expiry (#8720)

- **Commit:** `45875648`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-07-29T13:58:09+05:30
- **Changes:** 35 files (+283/-200)

## 1539. fix(connector): [Worldpay] handle multiple ddc submission for CompleteAuthorize (#8741)

- **Commit:** `f6cdddcb`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-07-29T13:58:34+05:30
- **Changes:** 8 files (+557/-9)

## 1540. feat(routing): Add api-refs for new decision engine endpoints (#8709)

- **Commit:** `4dea30ff`
- **Author:** Gaurav Rawat <104276743+GauravRawat369@users.noreply.github.com>
- **Date:** 2025-07-29T16:18:51+05:30
- **Changes:** 11 files (+755/-121)

## 1541. fix(connector): [GLOBALPAY] Added Tokenization Flow for CITs (#8568)

- **Commit:** `f7bc33cd`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-07-29T18:09:58+05:30
- **Changes:** 21 files (+536/-1120)

## 1542. feat(connector): [Flexiti]Add support for flexiti connector  (#8743)

- **Commit:** `2bd8c9d1`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-07-30T04:48:28-07:00
- **Changes:** 44 files (+556/-113)

## 1543. feat(connector): [payload] add recurring payments (#8597)

- **Commit:** `64e6dc86`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-07-31T12:21:44+05:30
- **Changes:** 22 files (+392/-181)

## 1544. feat(connector): [facilitapay] fix refunds, add webhook and void support (#8778)

- **Commit:** `c38ce386`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-07-31T12:24:08+05:30
- **Changes:** 7 files (+367/-69)

## 1545. feat(authentication): added authentication sync api (#8596)

- **Commit:** `794dce16`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-07-31T12:50:43+05:30
- **Changes:** 17 files (+1283/-97)

## 1546. feat(router): introduce `feature`  and `feature_data` to gsm (#7771)

- **Commit:** `1fa20a9a`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-07-31T16:16:35+05:30
- **Changes:** 22 files (+757/-173)

## 1547. feat(connector): [katapult]add template code for katapult (#8783)

- **Commit:** `c6e4e720`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-07-31T04:37:16-07:00
- **Changes:** 22 files (+1412/-38)

## 1548. feat(core): Implement UCS based  upi for  paytm and phonepe (#8732)

- **Commit:** `01e94748`
- **Author:** Uzair Khan <29498864+maverox@users.noreply.github.com>
- **Date:** 2025-07-31T19:17:04+05:30
- **Changes:** 39 files (+3098/-51)

## 1549. feat(router): [worldpayvantiv] add support for moto flag for v1 and extend vantiv api contract (#8800)

- **Commit:** `8ac5e504`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-08-01T16:01:26+05:30
- **Changes:** 25 files (+347/-60)

## 1550. feat(connector): [BLUECODE] Added Bluecode Wallet QR Code Redirect Payment Method (#8762)

- **Commit:** `c749bd9c`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-08-01T18:11:09+05:30
- **Changes:** 61 files (+642/-129)

## 1551. feat: add ci support for mock server (#8742)

- **Commit:** `03bdcfea`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-08-01T18:13:23+05:30
- **Changes:** 15 files (+2684/-130)

## 1552. feat(router): add support for apple pay pre-decrypted token in the payments confirm call (#8815)

- **Commit:** `b91e6d95`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-08-05T12:31:35+05:30
- **Changes:** 35 files (+786/-248)

## 1553. feat(payment-methods): add filtering logic for payment method list v2 (#8606)

- **Commit:** `2e137716`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-08-05T12:38:37+05:30
- **Changes:** 16 files (+616/-187)

## 1554. chore: reorder v2 migrations folders (#8671)

- **Commit:** `c573f611`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-08-05T13:17:18+05:30
- **Changes:** 37 files (+198/-128)

## 1555. feat(core): populate UCS status_code in response headers (#8788)

- **Commit:** `2adf6c83`
- **Author:** Aishwariyaa Anand <124241367+Aishwariyaa-Anand@users.noreply.github.com>
- **Date:** 2025-08-05T13:29:05+05:30
- **Changes:** 19 files (+184/-139)

## 1556. feat(connector): [NMI] Add mandates flow (#8652)

- **Commit:** `6d235d78`
- **Author:** DEEPANSHU BANSAL <41580413+deepanshu-iiitu@users.noreply.github.com>
- **Date:** 2025-08-05T16:01:47+05:30
- **Changes:** 3 files (+290/-98)

## 1557. feat(core): Add L2_L3 Data Support  (#8828)

- **Commit:** `58a9c9f0`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-08-05T18:10:04+05:30
- **Changes:** 85 files (+1250/-40)

## 1558. feat(connector): [AUTHORIZEDOTNET] create connector customer flow added (#8774)

- **Commit:** `8818a9b3`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-08-05T18:16:36+05:30
- **Changes:** 12 files (+471/-209)

## 1559. fix(core): add fix for stopping multiple event locking idempotent logs (#8034)

- **Commit:** `312c7337`
- **Author:** Debarati Ghatak <88573135+dgeee13@users.noreply.github.com>
- **Date:** 2025-08-05T19:19:55+05:30
- **Changes:** 4 files (+472/-5)

## 1560. feat(core): Added additional authentication fields for 3ds external authentication (#8758)

- **Commit:** `89774f3a`
- **Author:** Debarati Ghatak <88573135+dgeee13@users.noreply.github.com>
- **Date:** 2025-08-05T23:22:09+05:30
- **Changes:** 26 files (+382/-61)

## 1561. feat(connector): [Barclaycard] Add Google Pay Payment Method (#8786)

- **Commit:** `434e7a7a`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-08-06T12:48:57+05:30
- **Changes:** 13 files (+437/-51)

## 1562. feat(core): Add support for Void after Capture (#8839)

- **Commit:** `57e92c9f`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-08-06T13:15:43+05:30
- **Changes:** 61 files (+1422/-87)

## 1563. feat(router): [worldpayvantiv] add dispute list sync and implement dispute (#8830)

- **Commit:** `640d0552`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-08-06T15:31:25+05:30
- **Changes:** 69 files (+3579/-215)

## 1564. feat(gRPC): build gRPC client interface to initiate communication with recovery-decider service (#8178)

- **Commit:** `654c15ee`
- **Author:** Aditya Chaurasia <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-08-06T19:00:42+05:30
- **Changes:** 22 files (+730/-44)

## 1565. feat(router): add support for partial authorization (#8833)

- **Commit:** `c354e62f`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-08-06T19:38:09+05:30
- **Changes:** 67 files (+537/-79)

## 1566. feat(connector): [WORLDPAYVANTIV] Populate Network Decline Error Code & Message (#8856)

- **Commit:** `e2bfce89`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-08-06T21:53:17+05:30
- **Changes:** 1 files (+245/-65)

## 1567. feat(connector): [FISERV] Added PayPal Redirect Payment Method (#8669)

- **Commit:** `b0b71935`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-08-08T14:45:54+05:30
- **Changes:** 12 files (+487/-144)

## 1568. feat(recovery): add support for custom billing api for v2 (#8838)

- **Commit:** `9e8df845`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-08-08T02:38:34-07:00
- **Changes:** 15 files (+622/-178)

## 1569. feat(router): add support for GooglePay pre-decrypted token in the payments confirm call  (#8865)

- **Commit:** `b7f42cbd`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-08-08T17:09:24+05:30
- **Changes:** 45 files (+806/-229)

## 1570. feat(checkbook_io): connector integrate ACH (#8730)

- **Commit:** `bee4aed4`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-08-08T18:18:14+05:30
- **Changes:** 25 files (+582/-613)

## 1571. feat(connector): [SIFT] add Connector Template Code  (#8488)

- **Commit:** `2d3abd71`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-08-08T18:24:29+05:30
- **Changes:** 22 files (+1378/-12)

## 1572. refactor(euclid): refactor logs for evaluation of equality for dynamic routing evaluate response (#8834)

- **Commit:** `ef27ac5c`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-08-08T18:26:55+05:30
- **Changes:** 2 files (+311/-38)

## 1573. feat(core): Adding integration for webhooks through UCS (#8814)

- **Commit:** `06dc66c6`
- **Author:** Amitsingh Tanwar <126856945+AmitsinghTanwar007@users.noreply.github.com>
- **Date:** 2025-08-08T19:51:09+05:30
- **Changes:** 5 files (+898/-321)

## 1574. feat(core/connector): introduce authentication token flow and add sepa bankdebit for nordea (#8133)

- **Commit:** `b46a838d`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-08-11T12:42:44+05:30
- **Changes:** 63 files (+2870/-529)

## 1575. feat(router): Add new api for delete tokenization record (#8361)

- **Commit:** `0e957854`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-08-11T15:58:36+05:30
- **Changes:** 17 files (+436/-29)

## 1576. feat(ucs): add gateway system {Direct | UnifiedConnectorSystem} in feature metadata for v1 (#8854)

- **Commit:** `d034fadb`
- **Author:** Uzair Khan <29498864+maverox@users.noreply.github.com>
- **Date:** 2025-08-11T19:13:15+05:30
- **Changes:** 13 files (+313/-19)

## 1577. feat(payouts): add payout webhooks for Paypal and Wise (#8888)

- **Commit:** `fdc102de`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-08-11T19:14:38+05:30
- **Changes:** 5 files (+520/-16)

## 1578. feat(connector): [STRIPE] Add Incremental Authorization Flow (#8569)

- **Commit:** `e36bb99d`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-08-12T12:27:50+05:30
- **Changes:** 9 files (+303/-29)

## 1579. feat(connector): [FISERV] Added ApplePay Wallet (#8670)

- **Commit:** `8bb8b206`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-08-12T12:36:51+05:30
- **Changes:** 11 files (+395/-12)

## 1580. feat(core): add support for api locking with multiple keys for a single api (#8887)

- **Commit:** `2f7cd4f7`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-08-13T13:13:15+05:30
- **Changes:** 5 files (+663/-18)

## 1581. feat(connector): [NUVEI] Added support for AVC CVV checks, post confirm void and 0$ txns (#8766)

- **Commit:** `a132cb57`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-08-13T15:24:05+05:30
- **Changes:** 4 files (+882/-238)

## 1582. fix(connectors): [worldpayvantiv] add setup mandate flow, map network txn id and fix mandate flow (#8929)

- **Commit:** `6950c04e`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-08-13T19:40:16+05:30
- **Changes:** 6 files (+392/-90)

## 1583. refactor(config): change UCS connector list from array to comma-separated string (#8905)

- **Commit:** `9f055e10`
- **Author:** Uzair Khan <29498864+maverox@users.noreply.github.com>
- **Date:** 2025-08-13T20:24:27+05:30
- **Changes:** 10 files (+206/-12)

## 1584. feat(connector): [Hyperwallet] template code (#8926)

- **Commit:** `b797d934`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-08-14T13:43:12+05:30
- **Changes:** 23 files (+1403/-27)

## 1585. feat(router): Add support for confirm-intent external vault proxy flow (#8923)

- **Commit:** `7f648379`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-08-18T16:39:43+05:30
- **Changes:** 37 files (+3262/-89)

## 1586. refactor(connector): implement amount converter framework for bambora, dlocal and opennode  (#8883)

- **Commit:** `96f92531`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-08-18T19:57:44+05:30
- **Changes:** 10 files (+129/-89)

## 1587. refactor(connector): implement amount converter framework for coinbase, dummyconnector and gocardless (#8915)

- **Commit:** `79dcec46`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-08-18T20:02:06+05:30
- **Changes:** 10 files (+194/-93)

## 1588. feat: added create endpoint for dynamic_routing (#8755)

- **Commit:** `58abb604`
- **Author:** AnkitKmrGupta <143015358+AnkitKmrGupta@users.noreply.github.com>
- **Date:** 2025-08-19T13:08:36+05:30
- **Changes:** 8 files (+410/-10)

## 1589. refactor(connector): [AdyenPlatform] update required fields (#8990)

- **Commit:** `72eb25f0`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-08-19T16:12:23+05:30
- **Changes:** 2 files (+150/-160)

## 1590. feat(connector): [DWOLLA] Connector integration (#8586)

- **Commit:** `c09c9366`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-08-20T13:17:51+05:30
- **Changes:** 206 files (+1760/-331)

## 1591. feat(payment-methods): [Proxy] add saved card flow for proxy payments (#8964)

- **Commit:** `73dfa5e4`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-08-20T16:47:26+05:30
- **Changes:** 21 files (+861/-29)

## 1592. feat(connector): [CELERO] Integrate Card Payments (Alpha) (#8574)

- **Commit:** `e1fc1413`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-08-20T17:45:34+05:30
- **Changes:** 20 files (+6224/-1069)

## 1593. feat(connector): [barclaycard] Implement 3DS flow for cards (#8936)

- **Commit:** `19db2b5c`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-08-21T15:56:42+05:30
- **Changes:** 19 files (+2230/-96)

## 1594. feat(payments): add PaymentListFilterConstraints and payments_list_by_filter endpoint for v2 (#8794)

- **Commit:** `47ae9908`
- **Author:** Ayush Anand <114248859+ayush22667@users.noreply.github.com>
- **Date:** 2025-08-21T19:20:59+05:30
- **Changes:** 10 files (+218/-178)

## 1595. feat(connector): add integration status to feature matrix  (#8351)

- **Commit:** `6d984d48`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-08-21T20:12:08+05:30
- **Changes:** 119 files (+1499/-213)

## 1596. feat(nuvei): Googlepay , applepay and partial authorization integration for nuvei (#8985)

- **Commit:** `049e6b57`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-08-22T17:15:19+05:30
- **Changes:** 5 files (+558/-190)

## 1597. refactor(user_roles): implement parent group info based role APIs (#8896)

- **Commit:** `e3c46b7d`
- **Author:** Kanika Bansal <kanika.bansal@juspay.in>
- **Date:** 2025-08-22T18:38:23+05:30
- **Changes:** 11 files (+415/-103)

## 1598. feat(router): add support to use signature_network and is_issuer_regulated as filters (#9033)

- **Commit:** `ad05dc41`
- **Author:** Shankar Singh C <83439957+ShankarSinghC@users.noreply.github.com>
- **Date:** 2025-08-22T19:16:19+05:30
- **Changes:** 27 files (+158/-45)

## 1599. feat(connector): [BHN] Add BHN GiftCard Flow( Alpha) (#8701)

- **Commit:** `cb34ec51`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-08-22T22:00:03+05:30
- **Changes:** 36 files (+793/-444)

## 1600. feat(connector): [AFFIRM] BNPL flow added (Alpha) (#8795)

- **Commit:** `ad247b76`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-08-25T01:29:51+05:30
- **Changes:** 24 files (+1380/-137)

## 1601. feat(revenue_recovery): Add redis-based payment processor token tracking for revenue recovery (#8846)

- **Commit:** `0b59b908`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-08-25T14:58:39+05:30
- **Changes:** 24 files (+1364/-172)

## 1602. feat(connector): Add VGS connector impls (#7942)

- **Commit:** `ddf1a6a5`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-08-25T15:07:21+05:30
- **Changes:** 14 files (+254/-497)

## 1603. feat(revenue_recovery): Introducing new calculate job for card switching and invoice queueing (#8848)

- **Commit:** `5efe4d97`
- **Author:** Aditya Chaurasia <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-08-25T18:13:44+05:30
- **Changes:** 8 files (+1148/-121)

## 1604. feat(connector): [Adyenplatform] process payouts using PSP tokens (#9040)

- **Commit:** `b8c5bf3f`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-08-25T18:27:46+05:30
- **Changes:** 7 files (+350/-136)

## 1605. feat(injector): add support for new crate -  injector for external vault proxy (#8959)

- **Commit:** `d18a9418`
- **Author:** Shivansh Mathur <104988143+su-shivanshmathur@users.noreply.github.com>
- **Date:** 2025-08-25T18:41:42+05:30
- **Changes:** 6 files (+1204/-2)

## 1606. feat(connector): [Paysafe] add connector template code (#9011)

- **Commit:** `ce0159b6`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-08-26T12:18:51+05:30
- **Changes:** 22 files (+1395/-25)

## 1607. refactor(connector): implement amount converter framework for authorizedotnet, bankofamerica (#8878)

- **Commit:** `30925ca5`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-08-26T12:35:51+05:30
- **Changes:** 8 files (+125/-100)

## 1608. feat(connector): [Nuvei] Implement setup mandate flow for cards (#9012)

- **Commit:** `58ff01ba`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-08-26T17:34:41+05:30
- **Changes:** 8 files (+601/-101)

## 1609. feat(core): Added support for unified_connector_service CardNumber and Secret<String> Type (#9044)

- **Commit:** `cf64d2a9`
- **Author:** Debarshi Gupta <debarshi.gupta@juspay.in>
- **Date:** 2025-08-27T21:07:24+05:30
- **Changes:** 5 files (+186/-91)

## 1610. fix(revenue_recovery): Populate payment method data in record attempt flow for V2 (#9061)

- **Commit:** `594fae14`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-08-28T22:41:55+05:30
- **Changes:** 16 files (+486/-237)

## 1611. feat(connector): [AMAZONPAY] add Payment flows for Amazon Pay Wallet (#7062)

- **Commit:** `23cf4376`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-08-29T14:00:32+05:30
- **Changes:** 70 files (+1947/-271)

## 1612. feat(nuvei): NTID Support + googlepay & applepay mandate support (#9081)

- **Commit:** `a589e224`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-08-29T18:38:25+05:30
- **Changes:** 6 files (+276/-180)

## 1613. feat(injector): adding tracing to injector for dependency issues (#9124)

- **Commit:** `aae1994e`
- **Author:** Shivansh Mathur <104988143+su-shivanshmathur@users.noreply.github.com>
- **Date:** 2025-09-01T14:46:13+05:30
- **Changes:** 4 files (+179/-118)

## 1614. feat(core): [proxy payments] send external vault proxy metadata to UCS (#9108)

- **Commit:** `c02d8b9b`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-09-01T16:28:37+05:30
- **Changes:** 8 files (+244/-17)

## 1615. feat(connector): introduce setup mandate flow for payload (#9110)

- **Commit:** `4e33e974`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-09-01T16:49:26+05:30
- **Changes:** 3 files (+222/-69)

## 1616. feat(connector): Add Connector Specifications (#8797)

- **Commit:** `861e023f`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-09-01T17:49:57+05:30
- **Changes:** 31 files (+2001/-602)

## 1617. fix(authentication): fixed ctp confirmation bug (#9050)

- **Commit:** `44137517`
- **Author:** Sahkal Poddar <sahkalplanet@gmail.com>
- **Date:** 2025-09-01T18:39:40+05:30
- **Changes:** 9 files (+108/-119)

## 1618. fix(payments): automatic connector_payment_id hashing in v2 if length > 128 (#9017)

- **Commit:** `97ae3203`
- **Author:** Ayush Anand <114248859+ayush22667@users.noreply.github.com>
- **Date:** 2025-09-01T19:45:49+05:30
- **Changes:** 2 files (+394/-110)

## 1619. feat(ucs): add event logging for UCS operations (#9058)

- **Commit:** `10cf161d`
- **Author:** kanikac199 <143062617+kanikac199@users.noreply.github.com>
- **Date:** 2025-09-02T13:30:35+05:30
- **Changes:** 5 files (+314/-133)

## 1620. feat(core): Update payment methods api (#9075)

- **Commit:** `64511365`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2025-09-02T18:07:15+05:30
- **Changes:** 9 files (+404/-2)

## 1621. feat(connector): [SANTANDER] Added Boleto Payment Method (#9008)

- **Commit:** `63857a86`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-09-03T17:50:55+05:30
- **Changes:** 21 files (+1339/-174)

## 1622. feat(core): add subscription table (#9133)

- **Commit:** `144f3852`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-09-03T18:33:44+05:30
- **Changes:** 12 files (+379/-1)

## 1623. chore: Updated openapi spec added labels to wallet data (#9287)

- **Commit:** `c3ea9412`
- **Author:** sandeep-kuppili <kupili.reddy@juspay.in>
- **Date:** 2025-09-08T12:49:55+05:30
- **Changes:** 3 files (+313/-210)

## 1624. fix(payout): use billing address in payment_methods (#9277)

- **Commit:** `831100c0`
- **Author:** Kashif <kashif.dev@protonmail.com>
- **Date:** 2025-09-08T16:44:57+05:30
- **Changes:** 4 files (+142/-78)

## 1625. feat(connector): [Paysafe] Integrate no 3ds card (#9127)

- **Commit:** `439936da`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-08T21:30:29+05:30
- **Changes:** 21 files (+1645/-135)

## 1626. feat(router): add support for overcapture (#8949)

- **Commit:** `04a8cc44`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-09-09T14:46:01+05:30
- **Changes:** 45 files (+857/-83)

## 1627. feat(connector): [Barclaycard] Add Apple Pay Flow (#8885)

- **Commit:** `77498ee5`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-09-09T14:51:34+05:30
- **Changes:** 11 files (+423/-4)

## 1628. refactor(ucs): introduce dedicated gRPC header type and enhance lineage ID handling (#9275)

- **Commit:** `876ea3f6`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-09-09T14:51:55+05:30
- **Changes:** 11 files (+147/-67)

## 1629. fix(connectors): [authorizedotnet] send customerProfileId in the CIT flow and map customerPaymentProfileId in the Setup Mandate flow (#9298)

- **Commit:** `72c0f896`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-09-09T16:04:01+05:30
- **Changes:** 1 files (+150/-94)

## 1630. feat(connector): [checkout] Add mandate flow (#9248)

- **Commit:** `7355a83e`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-09-10T13:32:41+05:30
- **Changes:** 12 files (+404/-170)

## 1631. feat(core): [Retry] MIT Retries (#8628)

- **Commit:** `c0e31d38`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-09-10T17:28:36+05:30
- **Changes:** 6 files (+339/-122)

## 1632. feat(connector): enhance ACI connector with comprehensive 3DS support - DRAFT (#8986)

- **Commit:** `b014b138`
- **Author:** Ben Janecke <benjanecke@gmail.com>
- **Date:** 2025-09-10T14:18:42+02:00
- **Changes:** 10 files (+990/-465)

## 1633. feat(connector): [checkout] add support for MOTO payments (#9327)

- **Commit:** `3f8943bd`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-09-10T18:15:54+05:30
- **Changes:** 3 files (+337/-31)

## 1634. refactor(connector): rename RevenueRecoveryRecordBack as InvoiceRecordBack (#9321)

- **Commit:** `ea2fd1d4`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-09-10T18:54:19+05:30
- **Changes:** 21 files (+165/-196)

## 1635. fix(revenue-recovery): Update Redis TTL for customer locks after token selection (#9282)

- **Commit:** `df47c019`
- **Author:** Aniket Burman <93077964+aniketburman014@users.noreply.github.com>
- **Date:** 2025-09-11T16:13:33+05:30
- **Changes:** 13 files (+202/-21)

## 1636. feat(injector): injector request formation changes (#9306)

- **Commit:** `fabe82d2`
- **Author:** Shivansh Mathur <104988143+su-shivanshmathur@users.noreply.github.com>
- **Date:** 2025-09-11T17:06:03+05:30
- **Changes:** 5 files (+1041/-423)

## 1637. fix(nuvei): nuvei 3ds fix + psync fix (#9279)

- **Commit:** `ebba12ec`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-09-11T19:09:31+05:30
- **Changes:** 3 files (+516/-233)

## 1638. feat(router): Add Connector changes for 3ds (v2) (#9117)

- **Commit:** `6b880e45`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-09-11T19:23:43+05:30
- **Changes:** 8 files (+1845/-139)

## 1639. feat(connector): [Paysafe] Implement card 3ds flow (#9305)

- **Commit:** `a87ab733`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-11T21:09:36+05:30
- **Changes:** 6 files (+591/-71)

## 1640. feat(connector): Add Peachpayments Template Code (#9363)

- **Commit:** `0873d930`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-09-11T21:39:06+05:30
- **Changes:** 29 files (+1432/-23)

## 1641. feat(webhooks): Provide outgoing webhook support for revenue recovery (#9294)

- **Commit:** `2db61538`
- **Author:** CHALLA NISHANTH BABU <115225644+NISHANTH1221@users.noreply.github.com>
- **Date:** 2025-09-11T22:29:30+05:30
- **Changes:** 14 files (+392/-137)

## 1642. feat(connector): [PeachPayments] Add Cards Flow (#9030)

- **Commit:** `f3635a2e`
- **Author:** Ben Janecke <benjanecke@gmail.com>
- **Date:** 2025-09-12T09:22:59+02:00
- **Changes:** 14 files (+1143/-284)

## 1643. feat: add hyperswitch ai chats table (#8831)

- **Commit:** `8ed3f7db`
- **Author:** Jeeva Ramachandran <120017870+JeevaRamu0104@users.noreply.github.com>
- **Date:** 2025-09-16T13:55:41+05:30
- **Changes:** 34 files (+743/-37)

## 1644. feat(connector): Add support for get plans for Chargebee (#9281)

- **Commit:** `f3ab3d63`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2025-09-16T17:09:06+05:30
- **Changes:** 21 files (+547/-36)

## 1645. fix(connector): [Peachpayments] Fix Bugs (#9393)

- **Commit:** `a8aaffc6`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-09-16T19:26:10+05:30
- **Changes:** 2 files (+128/-180)

## 1646. feat(router): Add gift card balance check endpoint (v2) (#9102)

- **Commit:** `21316596`
- **Author:** Anurag Thakur <anurag.thakur@juspay.in>
- **Date:** 2025-09-17T13:07:31+05:30
- **Changes:** 29 files (+1011/-88)

## 1647. fix(connector): [nuvei] pass state field in the request, network handling for proxy flow (#9351)

- **Commit:** `1b8cd9db`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-09-17T20:13:35+05:30
- **Changes:** 8 files (+1154/-58)

## 1648. feat(connector): [TRUSTPAYMENTS] Integrate cards non 3ds payments (#8705)

- **Commit:** `1987cb4e`
- **Author:** Ayush Anand <114248859+ayush22667@users.noreply.github.com>
- **Date:** 2025-09-18T13:25:20+05:30
- **Changes:** 18 files (+2288/-154)

## 1649. feat(connector): [Paysafe] implement Skrill wallet Payment Method (#9396)

- **Commit:** `85bc733d`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-18T13:34:56+05:30
- **Changes:** 10 files (+438/-96)

## 1650. feat(revenue_recovery): add support for updating additional card info data from csv to redis (#9233)

- **Commit:** `d98ffdfb`
- **Author:** AdityaWNL <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-09-18T16:33:32+05:30
- **Changes:** 14 files (+702/-94)

## 1651. feat(subscriptions): add route for creating subscription intent (#9123)

- **Commit:** `d32b4619`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-09-18T17:07:31+05:30
- **Changes:** 21 files (+354/-17)

## 1652. feat(connector): Create Customer for Chargebee (#9304)

- **Commit:** `e6706187`
- **Author:** Ankit Kumar Gupta <143015358+AnkitKmrGupta@users.noreply.github.com>
- **Date:** 2025-09-18T18:56:18+05:30
- **Changes:** 19 files (+352/-73)

## 1653. feat(connector): Add support for get plan prices for Chargebee (#9300)

- **Commit:** `e2f1a456`
- **Author:** spritianeja03 <146620839+spritianeja03@users.noreply.github.com>
- **Date:** 2025-09-19T13:13:49+05:30
- **Changes:** 16 files (+450/-96)

## 1654. fix(connectors): [Nuvei] payments, refunds and chargeback webhooks (#9378)

- **Commit:** `9654d18d`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-09-19T16:40:31+05:30
- **Changes:** 2 files (+749/-179)

## 1655. feat(nuvei): applepay decrypt at hyperswitch flow (#9431)

- **Commit:** `c59a66a5`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-09-19T16:41:07+05:30
- **Changes:** 5 files (+231/-99)

## 1656. feat: Implement subscription create for Chargebee (#9303)

- **Commit:** `d978afdc`
- **Author:** Gaurav Rawat <104276743+GauravRawat369@users.noreply.github.com>
- **Date:** 2025-09-19T19:03:31+05:30
- **Changes:** 15 files (+455/-31)

## 1657. feat(connector): [Tokenex] add template code (#9416)

- **Commit:** `40357ae2`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-09-22T14:25:17+05:30
- **Changes:** 23 files (+1382/-5)

## 1658. feat(connector): [Gigadat] Connector Template code (#9450)

- **Commit:** `1ae6c209`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-22T19:27:59+05:30
- **Changes:** 22 files (+1405/-29)

## 1659. feat(router): Add v2 payment cancellation flow (#9083)

- **Commit:** `617b3faa`
- **Author:** Ayush Anand <114248859+ayush22667@users.noreply.github.com>
- **Date:** 2025-09-22T19:28:56+05:30
- **Changes:** 17 files (+1389/-39)

## 1660. feat(router): Add external vault support in v1 payments flow (#9274)

- **Commit:** `e410af26`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-09-23T12:12:11+05:30
- **Changes:** 34 files (+1323/-316)

## 1661. feat(connector): [Tokenex]Add external vault insert and retrieve flows  (#9470)

- **Commit:** `62b64d84`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-09-23T12:46:39+05:30
- **Changes:** 16 files (+219/-452)

## 1662. feat: add invoice table (#9348)

- **Commit:** `61949c55`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-09-23T15:07:57+05:30
- **Changes:** 13 files (+389/-3)

## 1663. chore(injector): injector change for proxy (#9460)

- **Commit:** `97d034a2`
- **Author:** Shivansh Mathur <104988143+su-shivanshmathur@users.noreply.github.com>
- **Date:** 2025-09-23T19:18:10+05:30
- **Changes:** 3 files (+65/-179)

## 1664. feat(process_tracker): Add resume api to resume the tasks in process tracker for revenue_recovery (#9461)

- **Commit:** `a4b6df08`
- **Author:** Amisha Prabhat <55580080+Aprabhat19@users.noreply.github.com>
- **Date:** 2025-09-24T17:13:56+05:30
- **Changes:** 8 files (+201/-65)

## 1665. feat(connector): [checkout] Add NTID flow (#9449)

- **Commit:** `d6929280`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-09-24T18:39:00+05:30
- **Changes:** 10 files (+163/-111)

## 1666. fix: Map attempt_status_unspecified to None instead of Unresolved for HS<>UCS ErrorResponse (#9445)

- **Commit:** `e0fa7e9b`
- **Author:** Saptak Dutta <138141940+Saptak88@users.noreply.github.com>
- **Date:** 2025-09-24T19:04:51+05:30
- **Changes:** 7 files (+122/-107)

## 1667. feat(subscription): Add support to estimate for a subscription in chargebee (#9336)

- **Commit:** `a7518373`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-09-24T19:30:19+05:30
- **Changes:** 13 files (+390/-41)

## 1668. feat(connector): [paysafe] introduce applepay encrypt and predecrypt flow (#9358)

- **Commit:** `2e0da5c0`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-09-24T20:03:00+05:30
- **Changes:** 16 files (+771/-99)

## 1669. feat(connector): [Gigadat] integrate interac bank redirect payment method (#9525)

- **Commit:** `93b97ef5`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-25T12:10:30+05:30
- **Changes:** 23 files (+431/-220)

## 1670. fix(connector): [Tokenex] fix tokenize flow response handling for tokenex (#9528)

- **Commit:** `84f3013c`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-09-25T19:16:51+05:30
- **Changes:** 7 files (+213/-75)

## 1671. feat(subscriptions): Add Subscription confirm handler (#9353)

- **Commit:** `f02d1803`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-09-25T19:17:51+05:30
- **Changes:** 20 files (+1007/-63)

## 1672. feat(connector): [Tesouro] Add template code (#9555)

- **Commit:** `239b6d37`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-09-25T22:52:41+05:30
- **Changes:** 23 files (+1394/-9)

## 1673. feat(framework): Added smithy, smithy-core and smithy-generator crates (#9249)

- **Commit:** `0baae338`
- **Author:** Debarshi Gupta <debarshi.gupta@juspay.in>
- **Date:** 2025-09-26T12:55:39+05:30
- **Changes:** 10 files (+2093/-0)

## 1674. feat(finix): template code (#9557)

- **Commit:** `e45bad38`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-09-26T18:00:08+05:30
- **Changes:** 22 files (+1419/-45)

## 1675. feat(connector): Add Peachpayments Cypress (#9573)

- **Commit:** `e03c0096`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-09-29T12:30:33+05:30
- **Changes:** 5 files (+693/-5)

## 1676. feat(connector): [ACI] cypress added (#9502)

- **Commit:** `1c52f699`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-09-29T12:42:14+05:30
- **Changes:** 4 files (+381/-78)

## 1677. feat(auth): add new authentication to communicate between microservices (#9547)

- **Commit:** `b8900d00`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-09-29T17:19:29+05:30
- **Changes:** 14 files (+214/-23)

## 1678. feat(core): Add support for partial auth in proxy payments [V2] (#9503)

- **Commit:** `c90744a6`
- **Author:** chikke srujan <121822803+srujanchikke@users.noreply.github.com>
- **Date:** 2025-09-30T12:07:57+05:30
- **Changes:** 21 files (+259/-59)

## 1679. feat(ucs): Add profile ID to lineage tracking in Unified Connector Service (#9559)

- **Commit:** `7654dbf4`
- **Author:** Hrithikesh <61539176+hrithikesh026@users.noreply.github.com>
- **Date:** 2025-09-30T12:24:12+05:30
- **Changes:** 11 files (+141/-68)

## 1680. feat(connector): [Loonio] Add template code (#9586)

- **Commit:** `5427b07a`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-30T12:34:35+05:30
- **Changes:** 22 files (+1401/-28)

## 1681. feat(payments): add tokenization action handling to payment flow for braintree (#9506)

- **Commit:** `efab34f0`
- **Author:** Ayush Anand <114248859+ayush22667@users.noreply.github.com>
- **Date:** 2025-09-30T12:56:58+05:30
- **Changes:** 3 files (+166/-41)

## 1682. feat(core): [Nuvei] add stored credentials flag  (#9515)

- **Commit:** `b776f92e`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-09-30T16:36:18+05:30
- **Changes:** 29 files (+257/-6)

## 1683. feat(connector): [Loonio] Implement interac Bank Redirect Payment Method (#9620)

- **Commit:** `c1f8b961`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-09-30T20:34:24+05:30
- **Changes:** 22 files (+307/-125)

## 1684. feat(payouts): [Nuvei] add payout flows (#9618)

- **Commit:** `3b5302c7`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-09-30T21:51:00+05:30
- **Changes:** 20 files (+574/-41)

## 1685. feat(security): add XSS and sqli validation for dashboard metadata fields (#9104)

- **Commit:** `cba489ff`
- **Author:** Kanika Bansal <kanika.bansal@juspay.in>
- **Date:** 2025-10-01T13:23:44+05:30
- **Changes:** 8 files (+506/-57)

## 1686. feat(connector): [Gigadat] Implement interac payouts (#9566)

- **Commit:** `cf30da2d`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-10-01T14:17:18+05:30
- **Changes:** 17 files (+510/-14)

## 1687. feat(connectors): [Tesouro] Integrate no-threeds cards (#9632)

- **Commit:** `fbd92fa1`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-10-01T17:46:24+05:30
- **Changes:** 21 files (+2617/-220)

## 1688. feat(revenue_recovery): add support to fetch data and update additional token data in redis (#9611)

- **Commit:** `af159867`
- **Author:** AdityaWNL <113281443+AdityaKumaar21@users.noreply.github.com>
- **Date:** 2025-10-01T20:29:52+05:30
- **Changes:** 10 files (+398/-9)

## 1689. feat(subscription): Add support to call payments microservice from subscription service via payments API client (#9590)

- **Commit:** `df663129`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-10-02T00:22:20+05:30
- **Changes:** 29 files (+1621/-624)

## 1690. feat: Implement subscriptions workflow and incoming webhook support (#9400)

- **Commit:** `32dd9e10`
- **Author:** Gaurav Rawat <104276743+GauravRawat369@users.noreply.github.com>
- **Date:** 2025-10-03T21:31:21+05:30
- **Changes:** 12 files (+381/-52)

## 1691. feat(subscriptions): Invoice record back workflow (#9529)

- **Commit:** `0a35c617`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-10-04T00:41:38+05:30
- **Changes:** 21 files (+950/-111)

## 1692. feat(connector): [tesouro] apple pay (#9648)

- **Commit:** `8375629c`
- **Author:** Pa1NarK <69745008+pixincreate@users.noreply.github.com>
- **Date:** 2025-10-07T13:03:40+05:30
- **Changes:** 11 files (+296/-7)

## 1693. feat(subscription): get plans for subscription (#9251)

- **Commit:** `b3beda7d`
- **Author:** Prajjwal Kumar <prajjwal.kumar@juspay.in>
- **Date:** 2025-10-07T13:18:59+05:30
- **Changes:** 15 files (+424/-21)

## 1694. feat(connector): [BRAINTREE] Googlepay, Applepay wallets added (#8728)

- **Commit:** `c172f03c`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-10-07T13:42:12+05:30
- **Changes:** 53 files (+998/-92)

## 1695. feat(core): Add support to update card exp in update payment methods api (#9688)

- **Commit:** `ad374997`
- **Author:** Mrudul Vajpayee <124863642+mrudulvajpayee4935@users.noreply.github.com>
- **Date:** 2025-10-07T17:11:04+05:30
- **Changes:** 4 files (+158/-89)

## 1696. feat(user_roles): add parent group info based API to fetch permissions for user role (#9487)

- **Commit:** `c44c3ed2`
- **Author:** Kanika Bansal <kanika.bansal@juspay.in>
- **Date:** 2025-10-07T19:25:31+05:30
- **Changes:** 10 files (+207/-93)

## 1697. fix(connector): [CALIDA] Changed Connector Name From Bluecode to Calida (#9712)

- **Commit:** `04a14e39`
- **Author:** Sayak Bhattacharya <sayakofficial21@gmail.com>
- **Date:** 2025-10-07T19:53:59+05:30
- **Changes:** 30 files (+307/-307)

## 1698. feat(connector): Loonio Webhooks (#9707)

- **Commit:** `27a7845a`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-10-07T22:28:41+05:30
- **Changes:** 2 files (+183/-35)

## 1699. feat(subscription): Add endpoint to get Subscription estimate (#9637)

- **Commit:** `15bc0a3b`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-10-08T18:46:38+05:30
- **Changes:** 13 files (+231/-24)

## 1700. feat(subscriptions): Add client secret auth support in subscriptions APIs (#9713)

- **Commit:** `01b4d6ae`
- **Author:** Sarthak Soni <76486416+Sarthak1799@users.noreply.github.com>
- **Date:** 2025-10-08T20:02:17+05:30
- **Changes:** 13 files (+177/-81)

## 1701. feat(connector): [Loonio] implement payouts (#9718)

- **Commit:** `abcc70be`
- **Author:** Swangi Kumari <85639103+swangi-kumari@users.noreply.github.com>
- **Date:** 2025-10-08T21:37:14+05:30
- **Changes:** 41 files (+915/-96)

## 1702. feat(connectors): [Paysafe] implement non-3DS card mandates (#9560)

- **Commit:** `35a20f8e`
- **Author:** AkshayaFoiger <131388445+AkshayaFoiger@users.noreply.github.com>
- **Date:** 2025-10-09T13:16:47+05:30
- **Changes:** 9 files (+512/-33)

## 1703. feat(subscription): domain_model for subscription and invoice (#9640)

- **Commit:** `17986c3b`
- **Author:** Ankit Kumar Gupta <143015358+AnkitKmrGupta@users.noreply.github.com>
- **Date:** 2025-10-09T15:13:56+05:30
- **Changes:** 15 files (+1093/-386)

## 1704. feat: introduce a framework to fetch configs from superposition (#9289)

- **Commit:** `acc1568b`
- **Author:** Shailesh <151172220+Shailesh-714@users.noreply.github.com>
- **Date:** 2025-10-09T15:41:52+05:30
- **Changes:** 18 files (+1571/-74)

## 1705. feat(connector): Card non3ds | FINIX (#9680)

- **Commit:** `5c6635be`
- **Author:** Nithin N <57832822+Nithin1506200@users.noreply.github.com>
- **Date:** 2025-10-09T18:10:06+05:30
- **Changes:** 22 files (+1698/-205)

## 1706. feat(connector): [BRAINTREE] Paypal wallet added (#8984)

- **Commit:** `f71090a9`
- **Author:** sweta-sharma <77436883+swetasharma03@users.noreply.github.com>
- **Date:** 2025-10-09T19:54:32+05:30
- **Changes:** 11 files (+212/-2)

## 1707. feat(framework): Added diff-checker required code and running ucs in shadow mode (#9684)

- **Commit:** `115ef10a`
- **Author:** Amitsingh Tanwar <126856945+AmitsinghTanwar007@users.noreply.github.com>
- **Date:** 2025-10-10T17:27:30+05:30
- **Changes:** 26 files (+1043/-315)

## 1708. feat(core): [NETWORK TOKENIZATION] Check Network Token Status API (#9443)

- **Commit:** `d9d4b2e5`
- **Author:** Sagnik Mitra <83326850+ImSagnik007@users.noreply.github.com>
- **Date:** 2025-10-10T17:27:47+05:30
- **Changes:** 13 files (+525/-20)

## 1709. feat(subscription): add support to create subscription with trial plans (#9721)

- **Commit:** `c2a9ce78`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-10-10T19:34:37+05:30
- **Changes:** 19 files (+421/-189)

## 1710. feat(connector): [Peach Payments] add network token support for connector (#9754)

- **Commit:** `c2da9db9`
- **Author:** Prasunna Soppa <70575890+prasunna09@users.noreply.github.com>
- **Date:** 2025-10-13T17:31:09+05:30
- **Changes:** 8 files (+284/-81)

## 1711. feat(core): add support for upi_intent and upi_qr (#9716)

- **Commit:** `5c7a6073`
- **Author:** kanikac199 <143062617+kanikac199@users.noreply.github.com>
- **Date:** 2025-10-13T18:01:53+05:30
- **Changes:** 29 files (+197/-23)

## 1712. feat(subscriptions): Add update subscriptions APIs with payments update call (#9778)

- **Commit:** `36fbaa07`
- **Author:** Gaurav Rawat <104276743+GauravRawat369@users.noreply.github.com>
- **Date:** 2025-10-14T15:42:48+05:30
- **Changes:** 21 files (+461/-86)

## 1713. refactor(db_interfaces): move db interfaces in router to domain_models (#9830)

- **Commit:** `59628332`
- **Author:** Jagan <jaganelavarasan@gmail.com>
- **Date:** 2025-10-15T12:18:53+05:30
- **Changes:** 55 files (+5385/-4503)

## 1714. feat(connector): [Peachpayments] Add Webhook Flow and Support For merchant_order_reference_id (#9781)

- **Commit:** `6394c892`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-10-15T16:29:55+05:30
- **Changes:** 2 files (+219/-49)

## 1715. fix(connector): Add WASM Changes for Finix Google Pay (#9845)

- **Commit:** `e641ea29`
- **Author:** Anurag <anuragsingh6501@gmail.com>
- **Date:** 2025-10-15T19:36:47+05:30
- **Changes:** 7 files (+226/-43)

## 1716. feat(router): add pre-confirm payments eligibility api (#9774)

- **Commit:** `ecf702ab`
- **Author:** Sai Harsha Vardhan <56996463+sai-harsha-vardhan@users.noreply.github.com>
- **Date:** 2025-10-16T12:05:31+05:30
- **Changes:** 12 files (+439/-63)

## 1717. feat(payouts): apple pay decrypt payout (#9857)

- **Commit:** `e7dee751`
- **Author:** Sakil Mostak <73734619+Sakilmostak@users.noreply.github.com>
- **Date:** 2025-10-16T12:29:32+05:30
- **Changes:** 22 files (+818/-4)

## 1718. feat(customers): add time range filtering and count functionality to customer list endpoints (#9767)

- **Commit:** `587588f8`
- **Author:** Venu Madhav Bandarupalli <110053886+VenuMadhav2541@users.noreply.github.com>
- **Date:** 2025-10-16T12:36:12+05:30
- **Changes:** 19 files (+482/-11)

## 1719. feat(connector): [Finix] Add support for Apple Pay (#9810)

- **Commit:** `2c4806d5`
- **Author:** Vani Gupta <118043711+Vani-1107@users.noreply.github.com>
- **Date:** 2025-10-16T12:41:58+05:30
- **Changes:** 13 files (+310/-28)

## 1720. feat(core): Add profile-level configuration for L2/L3 data enablement (#9683)

- **Commit:** `bd853345`
- **Author:** awasthi21 <107559116+awasthi21@users.noreply.github.com>
- **Date:** 2025-10-16T12:56:39+05:30
- **Changes:** 30 files (+158/-50)

