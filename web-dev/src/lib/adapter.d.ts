import EventEmitter from "eventemitter3";
import type { WalletError } from "./errors";
import type {
  SupportedTransactionVersions,
  DecryptPermission,
  WalletAdapterNetwork,
} from "./types";
export { EventEmitter };
export interface WalletAdapterEvents {
  connect(publicKey: string): void;
  disconnect(): void;
  error(error: WalletError): void;
  readyStateChange(readyState: WalletReadyState): void;
}
export declare type WalletName<T extends string = string> = T & {
  __brand__: "WalletName";
};
export interface WalletAdapterProps<Name extends string = string> {
  name: WalletName<Name>;
  url: string;
  icon: string;
  readyState: WalletReadyState;
  publicKey: string | null;
  viewKey: string | null;
  connecting: boolean;
  connected: boolean;
  supportedTransactionVersions: SupportedTransactionVersions;
  connect(
    decryptPermission: DecryptPermission,
    network: WalletAdapterNetwork
  ): Promise<void>;
  disconnect(): Promise<void>;
}
export declare type WalletAdapter<Name extends string = string> =
  WalletAdapterProps<Name> & EventEmitter<WalletAdapterEvents>;
/**
 * A wallet's readiness describes a series of states that the wallet can be in,
 * depending on what kind of wallet it is. An installable wallet (eg. a browser
 * extension like Phantom) might be `Installed` if we've found the Phantom API
 * in the global scope, or `NotDetected` otherwise. A loadable, zero-install
 * runtime (eg. Torus Wallet) might simply signal that it's `Loadable`. Use this
 * metadata to personalize the wallet list for each user (eg. to show their
 * installed wallets first).
 */
export declare enum WalletReadyState {
  /**
   * User-installable wallets can typically be detected by scanning for an API
   * that they've injected into the global context. If such an API is present,
   * we consider the wallet to have been installed.
   */
  Installed = "Installed",
  NotDetected = "NotDetected",
  /**
   * Loadable wallets are always available to you. Since you can load them at
   * any time, it's meaningless to say that they have been detected.
   */
  Loadable = "Loadable",
  /**
   * If a wallet is not supported on a given platform (eg. server-rendering, or
   * mobile) then it will stay in the `Unsupported` state.
   */
  Unsupported = "Unsupported",
}
export declare abstract class BaseWalletAdapter<Name extends string = string>
  extends EventEmitter<WalletAdapterEvents>
  implements WalletAdapter<Name>
{
  abstract name: WalletName<Name>;
  abstract url: string;
  abstract icon: string;
  abstract readyState: WalletReadyState;
  abstract publicKey: string | null;
  abstract viewKey: string | null;
  abstract connecting: boolean;
  abstract supportedTransactionVersions: SupportedTransactionVersions;
  get connected(): boolean;
  abstract connect(
    decryptPermission: DecryptPermission,
    network: WalletAdapterNetwork
  ): Promise<void>;
  abstract disconnect(): Promise<void>;
}
export declare function scopePollingDetectionStrategy(
  detect: () => boolean
): void;
