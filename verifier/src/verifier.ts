import { verifyCredential } from "@spruceid/didkit";

export const verify = (credential: any): boolean => {
  const proofPurpose = "assertionMethod";
  console.log(credential);
  const result = verifyCredential(credential, {
    proofPurpose,
  });
  console.log(result);
  if (result.errors.length > 0) {
    return false;
  } else {
    return true;
  }
};
