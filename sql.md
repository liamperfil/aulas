SELECT * FROM `estoque` WHERE `chNFe`='29240402303278000163550010000273181000648427';

DELETE FROM `estoque` WHERE `chNFe`='29240402303278000163550010000273181000648427';

```sql
INSERT INTO `estoque`(`id`, `codigo`, `descricao`, `ncm`, `cst`, `cfop`, `un`, `quantidade`, `valor`, `ean`, `nf`, `emit`, `uf`, `data`, `valornf`, `chNFe`, `destino`, `ipi`, `pisCofins`, `pICMS`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]','[value-11]','[value-12]','[value-13]','[value-14]','[value-15]','[value-16]','[value-17]','[value-18]','[value-19]','[value-20]')
```

```sql
SELECT id, codigo, descricao, ncm, MAX(cst) as cst_, cfop, un, SUM(quantidade) as qtd_, 
MAX(valor) as valor_, MAX(ean) as ean_, emit
FROM estoque
WHERE quantidade > 0
GROUP BY codigo, descricao
ORDER BY descricao ASC;
```

