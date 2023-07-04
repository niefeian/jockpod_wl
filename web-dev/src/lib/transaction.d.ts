export interface AleoTransition {
  program: string;
  functionName: string;
  inputs: any[];
  provingKeyUrl?: string;
}
export declare class Transition implements AleoTransition {
  program: string;
  functionName: string;
  inputs: any[];
  provingKeyUrl?: string;
  constructor(
    program: string,
    functionName: string,
    inputs: any[],
    provingKeyUrl?: string
  );
}
export interface AleoTransaction {
  address: string;
  chainId: string;
  transitions: AleoTransition[];
}
export declare class Transaction implements AleoTransaction {
  address: string;
  chainId: string;
  transitions: AleoTransition[];
  constructor(address: string, chainId: string, transitions: AleoTransition[]);
  static createTransaction(
    address: string,
    chainId: string,
    program: string,
    functionName: string,
    inputs: any[],
    provingKeyUrl?: string
  ): Transaction;
}
