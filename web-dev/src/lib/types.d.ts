export declare enum WalletAdapterNetwork {
  Testnet = "testnet3",
}
export declare type SupportedTransactionVersions = ReadonlySet<any> | null;
export declare type TransactionOrVersionedTransaction<
  S extends SupportedTransactionVersions
> = S extends null ? any : any | any;
export declare enum DecryptPermission {
  NoDecrypt = "NO_DECRYPT",
  UponRequest = "DECRYPT_UPON_REQUEST",
  AutoDecrypt = "AUTO_DECRYPT",
  ViewKeyAccess = "VIEW_KEY_ACCESS",
}
